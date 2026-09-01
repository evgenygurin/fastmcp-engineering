from pathlib import Path
import sys
from fastmcp.resources import resource

REPO_ROOT = Path(__file__).resolve().parents[2]
CONTRACTS_DIR = REPO_ROOT / "contracts"

def _contract_names() -> list[str]:
    return [p.stem for p in CONTRACTS_DIR.glob("*.md")]

# Expose each contract as contract://<stem>
# Use a resource template so completions can suggest names (Task 7).
@resource("contract://{name}")
def get_contract(name: str) -> str:
    path = CONTRACTS_DIR / f"{name}.md"
    if not path.exists():
        raise ValueError(f"Unknown contract: {name}. Valid: {', '.join(_contract_names())}")
    return path.read_text(encoding="utf-8")

def _make_static_getter(contract_path: Path):
    """Create a parameterless getter for a specific contract file."""
    def getter() -> str:
        return contract_path.read_text(encoding="utf-8")
    return getter

# Also register each contract as a static resource so it appears in list_resources()
for name in _contract_names():
    contract_path = CONTRACTS_DIR / f"{name}.md"
    getter = _make_static_getter(contract_path)
    # Wrap with resource decorator - getter has no parameters
    decorated = resource(f"contract://{name}")(getter)
    # Assign to module namespace so FileSystemProvider discovers it
    setattr(sys.modules[__name__], f"get_contract_{name.replace('-', '_')}", decorated)