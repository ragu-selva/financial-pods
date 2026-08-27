import { existsSync } from "node:fs";
import { join } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const projectRoot = fileURLToPath(new URL("..", import.meta.url));
const isWindows = process.platform === "win32";
const requestedTask = process.argv[2];
const supportedTasks = new Set([
  "setup",
  "dev",
  "lint",
  "format-check",
  "typecheck",
  "test",
  "build",
  "e2e",
  "up",
  "down",
  "logs",
  "stack-check",
  "stack-verify",
  "verify",
  "verify-artifacts",
]);

if (!supportedTasks.has(requestedTask)) {
  console.error(`Unknown task: ${requestedTask ?? "<missing>"}`);
  console.error(`Available tasks: ${[...supportedTasks].join(", ")}`);
  process.exit(2);
}

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    cwd: projectRoot,
    env: process.env,
    stdio: "inherit",
    shell: false,
    ...options,
  });

  if (result.error) {
    throw result.error;
  }
  if (result.status !== 0) {
    process.exit(result.status ?? 1);
  }
}

function runPnpm(args, options = {}) {
  if (process.env.npm_execpath) {
    run(process.execPath, [process.env.npm_execpath, ...args], options);
    return;
  }

  run("pnpm", args, { ...options, shell: isWindows });
}

function systemPython() {
  return process.env.FINANCIAL_PODS_PYTHON ?? (isWindows ? "python" : "python3");
}

function venvPython() {
  return join(
    projectRoot,
    ".venv",
    isWindows ? join("Scripts", "python.exe") : join("bin", "python"),
  );
}

function requireSetup() {
  if (!existsSync(venvPython())) {
    console.error("Python environment is missing. Run `node scripts/task.mjs setup` first.");
    process.exit(2);
  }
}

const webRoot = join(projectRoot, "apps/web");
const webCommands = {
  build: ["next/dist/bin/next", "build"],
  lint: ["eslint/bin/eslint.js", "."],
  "format:check": ["prettier/bin/prettier.cjs", "--check", "."],
  test: ["vitest/vitest.mjs", "run"],
  typecheck: ["typescript/bin/tsc", "--noEmit"],
};

const web = (script) => {
  const [entrypoint, ...args] = webCommands[script];
  run(process.execPath, [join(webRoot, "node_modules", entrypoint), ...args], { cwd: webRoot });
};
const apiModule = (module, args) => {
  requireSetup();
  run(venvPython(), ["-m", module, ...args], { cwd: join(projectRoot, "apps/api") });
};
const financeRoot = join(projectRoot, "packages/finance-engine");
const financeModule = (module, args) => {
  requireSetup();
  run(venvPython(), ["-m", module, ...args], { cwd: financeRoot });
};

switch (requestedTask) {
  case "setup":
    runPnpm(
      ["install", ...(existsSync(join(projectRoot, "pnpm-lock.yaml")) ? ["--frozen-lockfile"] : [])],
      { env: { ...process.env, CI: "true" } },
    );
    if (!existsSync(venvPython())) {
      run(systemPython(), ["-m", "venv", ".venv"]);
    }
    run(venvPython(), [
      "-m",
      "pip",
      "install",
      "--disable-pip-version-check",
      "-r",
      "apps/api/requirements-dev.lock",
    ]);
    break;
  case "dev":
  case "up":
    run("docker", ["compose", "up", "--build"]);
    break;
  case "down":
    run("docker", ["compose", "down", "--remove-orphans"]);
    break;
  case "logs":
    run("docker", ["compose", "logs", "--follow"]);
    break;
  case "stack-check":
    run(process.execPath, ["tests/integration/stack-health.mjs"]);
    break;
  case "stack-verify":
    run("docker", [
      "compose",
      "--env-file",
      ".env.example",
      "up",
      "--build",
      "--detach",
      "--wait",
      "--wait-timeout",
      "180",
    ]);
    run(process.execPath, ["tests/integration/stack-health.mjs"]);
    break;
  case "lint":
    for (const file of [
      "scripts/task.mjs",
      "scripts/run-web-e2e.mjs",
      "scripts/verify-reference-artifacts.mjs",
      "tests/integration/stack-health.mjs",
    ]) {
      run(process.execPath, ["--check", file]);
    }
    web("lint");
    apiModule("ruff", ["check", "."]);
    financeModule("ruff", ["check", "."]);
    break;
  case "format-check":
    web("format:check");
    apiModule("ruff", ["format", "--check", "."]);
    financeModule("ruff", ["format", "--check", "."]);
    break;
  case "typecheck":
    web("typecheck");
    apiModule("mypy", []);
    financeModule("mypy", []);
    break;
  case "test":
    web("test");
    apiModule("pytest", []);
    financeModule("pytest", []);
    break;
  case "build":
    web("build");
    apiModule("build", ["--no-isolation", "--outdir", "dist"]);
    financeModule("build", ["--no-isolation", "--outdir", "dist"]);
    break;
  case "e2e":
    run(process.execPath, ["scripts/run-web-e2e.mjs"]);
    break;
  case "verify":
    for (const task of [
      "format-check",
      "lint",
      "typecheck",
      "test",
      "build",
      "e2e",
      "verify-artifacts",
    ]) {
      run(process.execPath, ["scripts/task.mjs", task]);
    }
    break;
  case "verify-artifacts":
    run(process.execPath, ["scripts/verify-reference-artifacts.mjs"]);
    break;
}
