from pathlib import Path
from typing import Annotated
from fastmcp.tools import tool
from fastmcp import Context
from mcp.types import ElicitRequest, ElicitRequestFormParams, InputRequiredResult
from server.indexing import build_index, search_index

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS_ROOT = REPO_ROOT / "skills"

@tool
def find_skills(
    task: Annotated[str, "Task description to find relevant skills for"],
    domain: Annotated[str | None, "Optional domain filter"] = None,
    limit: Annotated[int, "Max results"] = 5,
) -> list[dict]:
    idx = build_index(SKILLS_ROOT)
    hits = search_index(idx, task, domain=domain, limit=limit)
    return [{"name": h.name, "description": h.description, "uri": h.uri, "domain": h.domain, "score": h.score} for h in hits]

@tool
async def clarify_find(
    task: Annotated[str, "Ambiguous task to clarify"],
    ctx: Context,
) -> str | InputRequiredResult:
    answers = getattr(ctx, "input_responses", None)
    if answers is None:
        # Check if task is ambiguous: low top score
        idx = build_index(SKILLS_ROOT)
        hits = search_index(idx, task, limit=1)
        if hits and hits[0].score < 2.0:
            params = ElicitRequestFormParams(
                message="Which domain is this task about?",
                requested_schema={
                    "type": "object",
                    "properties": {"domain": {"type": "string", "description": "Domain e.g. fastmcp, architecture, security"}},
                    "required": ["domain"],
                },
            )
            return InputRequiredResult(
                result_type="input_required",
                input_requests={"domain": ElicitRequest(method="elicitation/create", params=params)},
            )
        # Not ambiguous — return direct answer
        hits = search_index(idx, task, limit=5)
        return "\n".join(f"{h.name}: {h.description}" for h in hits)

    # Second round: user answered
    response = answers.get("domain")
    domain = None
    if response and response.action == "accept" and response.content:
        domain = response.content.get("domain")
    idx = build_index(SKILLS_ROOT)
    hits = search_index(idx, task, domain=domain, limit=5)
    return "\n".join(f"{h.name}: {h.description} ({h.uri})" for h in hits) or "No matches."