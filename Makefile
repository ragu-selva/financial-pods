.PHONY: setup dev lint format-check typecheck test build e2e up down logs stack-check stack-verify verify verify-artifacts

setup dev lint format-check typecheck test build e2e up down logs stack-check stack-verify verify verify-artifacts:
	node scripts/task.mjs $@
