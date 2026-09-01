import pytest
from fastmcp import Client
from server.server import mcp


@pytest.mark.asyncio
async def test_full_agent_flow():
    async with Client(mcp) as client:
        # 1. find
        r = await client.call_tool("find_skills", arguments={"task": "add OAuth to my server"})
        assert r.data and len(r.data) > 0
        top = r.data[0]["name"]
        # 2. read skill
        skill = await client.read_resource(f"skill://{top}/SKILL.md")
        assert len(skill[0].text) > 100
        # 3. get prompt context
        prompt = await client.get_prompt("skill_context", arguments={"skill": top})
        assert top in prompt.messages[0].content.text
        # 4. contract check prompt
        check = await client.get_prompt("contract_check", arguments={"contract": "skill-contract", "artifact": "dummy SKILL.md content"})
        assert "skill-contract" in check.messages[0].content.text.lower()