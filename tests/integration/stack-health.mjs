import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const projectRoot = fileURLToPath(new URL("../..", import.meta.url));
const expectedServices = new Set(["api", "postgres", "redis", "web"]);

function dockerCompose(args) {
  const result = spawnSync(
    "docker",
    ["compose", "--env-file", ".env.example", ...args],
    {
      cwd: projectRoot,
      encoding: "utf8",
      shell: false,
    },
  );

  if (result.error) {
    throw result.error;
  }
  if (result.status !== 0) {
    throw new Error(result.stderr || result.stdout || `Docker Compose exited ${result.status}.`);
  }
  return result.stdout.trim();
}

async function getJson(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`${url} returned HTTP ${response.status}.`);
  }
  return response.json();
}

const serviceRows = dockerCompose(["ps", "--format", "json"])
  .split(/\r?\n/)
  .filter(Boolean)
  .map((line) => JSON.parse(line));

for (const row of serviceRows) {
  if (row.State !== "running" || row.Health !== "healthy") {
    throw new Error(`${row.Service} is ${row.State}/${row.Health || "no-health-state"}.`);
  }
  expectedServices.delete(row.Service);
}
if (expectedServices.size > 0) {
  throw new Error(`Missing healthy services: ${[...expectedServices].join(", ")}.`);
}

const apiHealth = await getJson("http://127.0.0.1:8000/health");
if (
  apiHealth.status !== "ok" ||
  apiHealth.service !== "financial-pods-api" ||
  typeof apiHealth.trace_id !== "string"
) {
  throw new Error("API health response does not match the Sprint 00 contract.");
}

const webHealth = await getJson("http://127.0.0.1:3000/health");
if (webHealth.status !== "ok" || webHealth.service !== "financial-pods-web") {
  throw new Error("Web health response does not match the Sprint 00 contract.");
}

const page = await fetch("http://127.0.0.1:3000/").then((response) => response.text());
if (!page.includes("Financial Pods") || !page.includes("Product experiences are intentionally deferred")) {
  throw new Error("Web placeholder content is missing or product scope leaked into Sprint 00.");
}

const pgvector = dockerCompose([
  "exec",
  "--no-TTY",
  "postgres",
  "psql",
  "-U",
  "financial_pods",
  "-d",
  "financial_pods",
  "-tAc",
  "SELECT extversion FROM pg_extension WHERE extname = 'vector';",
]);
if (pgvector !== "0.8.1") {
  throw new Error(`Expected pgvector 0.8.1, received ${pgvector || "no result"}.`);
}

const redis = dockerCompose(["exec", "--no-TTY", "redis", "redis-cli", "ping"]);
if (redis !== "PONG") {
  throw new Error(`Expected Redis PONG, received ${redis || "no result"}.`);
}

console.log("Verified healthy web, API, PostgreSQL/pgvector, and Redis services.");
