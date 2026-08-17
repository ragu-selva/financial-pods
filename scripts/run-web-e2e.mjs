import { spawn, spawnSync } from "node:child_process";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const projectRoot = fileURLToPath(new URL("..", import.meta.url));
const webRoot = join(projectRoot, "apps", "web");
const port = process.env.FINANCIAL_PODS_E2E_PORT ?? "3100";
const baseUrl = `http://127.0.0.1:${port}`;
const nextEntrypoint = join(webRoot, "node_modules", "next", "dist", "bin", "next");
const playwrightEntrypoint = join(
  webRoot,
  "node_modules",
  "@playwright",
  "test",
  "cli.js",
);

const server = spawn(
  process.execPath,
  [nextEntrypoint, "dev", "--hostname", "127.0.0.1", "--port", port],
  {
    cwd: webRoot,
    env: { ...process.env, NEXT_TELEMETRY_DISABLED: "1" },
    stdio: "inherit",
    detached: process.platform !== "win32",
  },
);

function stopServer() {
  if (server.exitCode !== null || server.pid === undefined) {
    return;
  }

  if (process.platform === "win32") {
    spawnSync("taskkill", ["/pid", String(server.pid), "/t", "/f"], {
      stdio: "ignore",
      windowsHide: true,
    });
  } else {
    process.kill(-server.pid, "SIGTERM");
  }
}

async function waitForHealth() {
  const deadline = Date.now() + 120_000;
  while (Date.now() < deadline) {
    if (server.exitCode !== null) {
      throw new Error(`Next.js test server exited with code ${server.exitCode}.`);
    }

    try {
      const response = await fetch(`${baseUrl}/health`);
      if (response.ok) {
        return;
      }
    } catch {
      // The server is still starting.
    }

    await new Promise((resolve) => setTimeout(resolve, 500));
  }

  throw new Error(`Timed out waiting for ${baseUrl}/health.`);
}

process.once("SIGINT", () => {
  stopServer();
  process.exit(130);
});
process.once("SIGTERM", () => {
  stopServer();
  process.exit(143);
});

let exitCode = 1;
try {
  await waitForHealth();
  const result = spawnSync(process.execPath, [playwrightEntrypoint, "test"], {
    cwd: webRoot,
    env: {
      ...process.env,
      PLAYWRIGHT_BASE_URL: baseUrl,
      PLAYWRIGHT_EXTERNAL_SERVER: "1",
    },
    stdio: "inherit",
  });

  if (result.error) {
    throw result.error;
  }
  exitCode = result.status ?? 1;
} finally {
  stopServer();
}

process.exit(exitCode);
