import { createHash } from "node:crypto";
import { createReadStream, existsSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const projectRoot = fileURLToPath(new URL("..", import.meta.url));
const expectedArtifacts = new Map([
  [
    "docs/reference-artifacts/research/Financial_Pods_Master_Strategy_Research_and_Implementation_Blueprint.docx",
    "40E3B48D84E8B5521B9AA112145D4E19F41EED78A92517A4D7BD2680182153E2",
  ],
  [
    "docs/reference-artifacts/specifications/Financial_Pods_V1_Technical_and_Functional_Specification.docx",
    "B91F9297CC7CA33FD2FDBD38C6AADF43CC41B08FC545A441455D208A8C44E7C6",
  ],
  [
    "docs/reference-artifacts/engineering/Financial_Pods_Engineering_Deployment_and_Coding_Playbook.docx",
    "059F5ABC282CF871DFEC09DBED7292C39F505481ADE67D88CAD0514404726531",
  ],
  [
    "docs/reference-artifacts/engineering/Prudential_Capital_Change_Assurance_Final_Implementation_Plan.docx",
    "9F62FAE740C32335CA4436FA6FFFB0077D9ACF8DE6D8866373993402F21D91C1",
  ],
  [
    "docs/reference-artifacts/growth/Financial_Pods_Content_Growth_and_Publishing_Strategy.docx",
    "099BDDE14064317565CE849DB88B7D01273708D92B1423AE4B899BEE71A50899",
  ],
  [
    "docs/reference-artifacts/growth/Financial_Pods_Content_Growth_and_Publishing_Strategy.pdf",
    "C92F9817917FF563E726EBCEF102142F492F12003DD378365CE278FB326988FE",
  ],
  [
    "docs/reference-artifacts/deck/Financial_Pods_Strategy_and_Implementation_Deck.pptx",
    "236DA81CA74998E9E61612881C03D5A7DDD973D193CDF8E428953575B22A11EA",
  ],
  [
    "docs/reference-artifacts/prototype/Financial_Pods_Golden_Lesson_UI_Prototype.html",
    "2111E2F54906B5995D92DC13230AEC8BF67228CA7D43B0DC1429A754358830DE",
  ],
  [
    "docs/reference-artifacts/source-packages/Financial_Pods_Developer_Agent_Starter_Pack.zip",
    "F8110E7A057079C59A5674734A933E7B0BFB39CB088D738986A7543E6BB0E7CF",
  ],
  [
    "docs/reference-artifacts/source-packages/Financial-Pods-Codex-Package.zip",
    "86E170637E352B0BAB37C08CA886AB0051E126C0CAF9CA9ADB959CB89451F38E",
  ],
]);

async function sha256(path) {
  const hash = createHash("sha256");
  for await (const chunk of createReadStream(path)) {
    hash.update(chunk);
  }
  return hash.digest("hex").toUpperCase();
}

const failures = [];
for (const [relativePath, expectedHash] of expectedArtifacts) {
  const path = join(projectRoot, ...relativePath.split("/"));
  if (!existsSync(path)) {
    failures.push(`Missing: ${relativePath}`);
    continue;
  }

  const actualHash = await sha256(path);
  if (actualHash !== expectedHash) {
    failures.push(`Checksum mismatch: ${relativePath}`);
  }
}

if (failures.length > 0) {
  for (const failure of failures) {
    console.error(failure);
  }
  process.exit(1);
}

console.log(`Verified ${expectedArtifacts.size} immutable reference artifacts.`);
