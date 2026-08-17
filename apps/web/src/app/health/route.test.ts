// @vitest-environment node

import { describe, expect, it } from "vitest";

import { GET } from "./route";

describe("GET /health", () => {
  it("returns the stable web-service health payload", async () => {
    const response = GET();

    expect(response.status).toBe(200);
    expect(response.headers.get("cache-control")).toBe("no-store");
    await expect(response.json()).resolves.toEqual({
      status: "ok",
      service: "financial-pods-web",
      version: "0.0.0",
    });
  });
});
