# FastMCP Engineering Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Each task is independently reviewable.

**Goal:** Establish the research-first engineering system that future FastMCP skills will use to design, implement, test, review, and verify production MCP servers.

**Architecture:** The repository is methodology-first. Skills are adapters around explicit contracts and research artifacts; an Architecture Governor enforces dependency direction and responsibility boundaries. FastMCP remains the MCP delivery/runtime layer, while domain, application, and infrastructure concerns stay independently testable.

**Tech Stack:** Python 3.10+, FastMCP 3.x production baseline, MCP specification, Pydantic, SQLAlchemy 2.x, PydanticAI where justified, Supabase where justified, pytest, ruff, mypy/pyright as project-specific choices, GitHub Actions.

**Spec:** `docs/specs/engineering-system.md`

## Global Constraints

- Research official FastMCP documentation and the official FastMCP repository examples before selecting a FastMCP mechanism.
- Production guidance targets the latest stable FastMCP 3.x line; FastMCP 4.x is tracked separately and must never be silently mixed into 3.x guidance.
- Domain code must not depend on FastMCP, SQLAlchemy, PydanticAI, Supabase, HTTP clients, or MCP transport details.
- MCP handlers are adapters and must not own business logic or persistence orchestration.
- Prefer native FastMCP Providers, Transforms, Middleware, Context, lifespan, tasks, auth, authorization, pagination, versioning, telemetry, and Client capabilities before inventing custom infrastructure.
- SOLID, KISS, DRY, and YAGNI are constraints, not excuses for speculative abstractions.
- Every non-trivial pattern requires a concrete problem, alternatives considered, and a reason the added complexity is justified.
- Every implementation must have an explicit verification strategy.

---

### Task 1: Establish engineering specification

**Files:**
- Create: `docs/specs/engineering-system.md`
- Create: `architecture/principles.md`
- Create: `architecture/dependency-rules.md`

**Interfaces:**
- Produces the normative rules consumed by every future skill.

- [ ] **Step 1: Define the system model**
- [ ] **Step 2: Define layer and dependency rules**
- [ ] **Step 3: Define version-policy and research gates**
- [ ] **Step 4: Review for KISS/YAGNI and remove speculative requirements**

### Task 2: Define research protocol

**Files:**
- Create: `research/fastmcp/version-policy.md`
- Create: `research/fastmcp/documentation-map.md`
- Create: `research/fastmcp/examples-catalog.md`
- Create: `research/fastmcp/pattern-catalog.md`

**Interfaces:**
- Produces evidence-backed artifacts that implementation skills must consume.

- [ ] **Step 1: Record official source hierarchy**
- [ ] **Step 2: Define example classification format**
- [ ] **Step 3: Define production-adaptation and anti-pattern fields**
- [ ] **Step 4: Record current findings from official FastMCP docs/examples**

### Task 3: Define skill and artifact contracts

**Files:**
- Create: `contracts/skill-contract.md`
- Create: `contracts/research-contract.md`
- Create: `contracts/verification-contract.md`

**Interfaces:**
- Skills consume research artifacts and emit explicit design/implementation/review artifacts.

- [ ] **Step 1: Define required skill inputs and outputs**
- [ ] **Step 2: Define evidence requirements**
- [ ] **Step 3: Define verification evidence**

### Task 4: Create foundation skills

**Files:**
- Create: `skills/foundation/research-first/SKILL.md`
- Create: `skills/architecture/architecture-governor/SKILL.md`
- Create: `skills/foundation/pattern-selection/SKILL.md`
- Create: `skills/foundation/final-review/SKILL.md`

**Interfaces:**
- These are the upstream gates for all specialized skills.

- [ ] **Step 1: Implement research-first gate**
- [ ] **Step 2: Implement architecture governor**
- [ ] **Step 3: Implement pattern justification gate**
- [ ] **Step 4: Implement final review gate**

### Task 5: Add reusable prompts

**Files:**
- Create: `prompts/research-agent.md`
- Create: `prompts/architecture-agent.md`
- Create: `prompts/implementation-agent.md`
- Create: `prompts/review-agent.md`

**Interfaces:**
- Prompts provide complete context to fresh subagents so skills can be developed in isolated sessions.

- [ ] **Step 1: Define research-agent prompt**
- [ ] **Step 2: Define architecture-agent prompt**
- [ ] **Step 3: Define implementation-agent prompt**
- [ ] **Step 4: Define review-agent prompt**

### Task 6: Add repository governance

**Files:**
- Modify: `README.md`
- Create: `AGENTS.md`
- Create: `CONTRIBUTING.md`
- Create: `.github/pull_request_template.md`

**Interfaces:**
- Repository-level instructions and review expectations.

- [ ] **Step 1: Document workflow**
- [ ] **Step 2: Document contribution gates**
- [ ] **Step 3: Document research evidence expectations**

### Task 7: Review and hand off

**Files:**
- Review all files created by Tasks 1-6.

- [ ] **Step 1: Check specification coverage**
- [ ] **Step 2: Check terminology consistency**
- [ ] **Step 3: Check for placeholders and speculative abstractions**
- [ ] **Step 4: Verify repository links and source references**
- [ ] **Step 5: Open a PR for foundation review**
