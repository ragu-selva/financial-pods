import { expect, test } from "@playwright/test";

test("renders the bootstrap shell", async ({ page }) => {
  await page.goto("/");

  await expect(
    page.getByRole("heading", { level: 1, name: "Financial Pods" }),
  ).toBeVisible();
  await expect(page.getByRole("status")).toHaveText("Web service operational");
});

test("reports web service health", async ({ request }) => {
  const response = await request.get("/health");

  expect(response.ok()).toBe(true);
  await expect(response.json()).resolves.toEqual({
    status: "ok",
    service: "financial-pods-web",
    version: "0.0.0",
  });
});
