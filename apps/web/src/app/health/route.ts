import { NextResponse } from "next/server";

const health = {
  status: "ok",
  service: "financial-pods-web",
  version: "0.0.0",
} as const;

export function GET() {
  return NextResponse.json(health, {
    status: 200,
    headers: {
      "Cache-Control": "no-store",
    },
  });
}
