import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

import Home from "./page";

describe("Home", () => {
  it("renders the accessible bootstrap placeholder", () => {
    render(<Home />);

    expect(
      screen.getByRole("heading", { level: 1, name: "Financial Pods" }),
    ).toBeInTheDocument();
    expect(screen.getByRole("status")).toHaveTextContent(
      "Web service operational",
    );
  });

  it("states that product functionality is deferred", () => {
    render(<Home />);

    expect(screen.getByText(/intentionally deferred/i)).toBeInTheDocument();
  });
});
