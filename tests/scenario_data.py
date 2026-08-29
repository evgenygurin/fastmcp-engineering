from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SkillScenario:
    skill: str
    positive_input: str
    positive_expected: str
    negative_input: str
    negative_expected: str


# Deterministic fixtures are intentionally framework-level: they verify that a
# skill package can state what success and safe failure look like without
# pretending that Markdown itself executes a FastMCP server.
REPRESENTATIVE_SCENARIOS = (
    SkillScenario(
        skill="fastmcp/auth",
        positive_input="Valid token: issuer=trusted, audience=mcp-api, scope=tools:read",
        positive_expected="Authenticate the principal and allow only the requested scope.",
        negative_input="Expired token with otherwise valid issuer and audience",
        negative_expected="Reject authentication; do not execute the protected operation.",
    ),
    SkillScenario(
        skill="fastmcp/client-testing",
        positive_input="Client connects through the declared transport and invokes a known tool.",
        positive_expected="Verify transport-specific behavior and the tool result.",
        negative_input="In-process call presented as proof of deployed HTTP/stdio behavior",
        negative_expected="Reject the evidence claim and require transport-level verification.",
    ),
    SkillScenario(
        skill="fastmcp/protocol-compliance",
        positive_input="Capability and method match the applicable MCP specification version.",
        positive_expected="Verify protocol semantics against authoritative specification evidence.",
        negative_input="Framework behavior conflicts with the applicable MCP specification.",
        negative_expected="Stop and escalate rather than treating framework behavior as protocol truth.",
    ),
)
