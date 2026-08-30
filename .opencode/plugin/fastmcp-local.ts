import type { Plugin } from "@opencode-ai/plugin"

export default (async () => {
  return {
    "tool.execute.before": async (input, output) => {
      const args = (output as { args?: Record<string, unknown> }).args
      if (input.tool === "task" && args?.prompt && typeof args.prompt === "string") {
        const p = (args.prompt as string).toLowerCase()
        if (p.includes("fastmcp") || p.includes("mcp server") || p.includes("mcp tool")) {
          args.prompt = (args.prompt as string) + "\n\n[fastmcp-engineering:local] Refer to @fastmcp-eng for architecture principles, engineering contracts, and research-first workflow before implementing."
        }
      }
    }
  }
}) satisfies Plugin
