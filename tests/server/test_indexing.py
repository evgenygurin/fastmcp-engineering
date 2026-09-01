from pathlib import Path
from server.indexing import build_index, search_index

def test_index_finds_58_skills():
    idx = build_index(Path("skills"))
    assert len(idx.entries) == 58
    names = {e.name for e in idx.entries}
    assert "architecture-governor" in names
    assert "fastmcp-auth" in names

def test_search_weights_name_over_body():
    idx = build_index(Path("skills"))
    hits = search_index(idx, "auth", limit=5)
    assert hits[0].name == "fastmcp-auth"
    assert hits[0].score > hits[1].score

def test_domain_filter():
    idx = build_index(Path("skills"))
    hits = search_index(idx, "auth", domain="fastmcp", limit=10)
    assert all(h.domain == "fastmcp" for h in hits)
