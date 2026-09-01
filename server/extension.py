from typing import Any
from mcp.types import RequestParams
from fastmcp.server.extensions import MethodBinding, ServerExtension
from pathlib import Path


class StatsParams(RequestParams):
    pass


class MethodologyExtension(ServerExtension):
    identifier = "dev.fastmcp-eng/methodology"

    def __init__(self) -> None:
        self.call_counts: dict[str, int] = {}

    def settings(self) -> dict[str, Any]:
        from server.indexing import build_index
        idx = build_index(Path("skills"))
        domains = sorted({e.domain for e in idx.entries})
        return {"skillsCount": len(idx.entries), "domains": domains, "version": "0.1.0"}

    def methods(self) -> list[MethodBinding]:
        return [MethodBinding(method="methodology/stats", params_type=StatsParams, handler=self.get_stats)]

    async def get_stats(self, ctx, params: StatsParams) -> dict[str, Any]:
        from server.indexing import build_index
        idx = build_index(Path("skills"))
        return {"skillsCount": len(idx.entries), "domains": sorted({e.domain for e in idx.entries}), "callCounts": dict(self.call_counts)}

    async def intercept_tool_call(self, params, context, call_next):
        # Interceptor — count calls, then delegate
        name = getattr(params, "name", "unknown")
        self.call_counts[name] = self.call_counts.get(name, 0) + 1
        return await call_next()