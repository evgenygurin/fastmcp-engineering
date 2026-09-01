---
name: research-first
description: Enforce research-first workflow before any framework-sensitive change — use to prevent implementation based on stale APIs or assumptions.
---

# Research First

## Purpose

Prevent implementation based on memory, assumptions, stale APIs, or incomplete examples.

## Trigger / Когда применять

**Scope / When to use:** before any task that changes FastMCP behavior, MCP contracts, integrations, security, persistence, transport, lifecycle, or other framework-sensitive behavior.
**Trigger:** any framework-sensitive change; requirement unclear; version not identified; official docs not yet consulted.
**Upstream / Prerequisite:** a clarified requirement; identified target versions; repository contracts and AGENTS.md.
**Mission / Goal:** prevent implementation based on memory, assumptions, stale APIs, or incomplete examples.
**Research / Evidence:** read official FastMCP documentation, official examples and tests, the MCP specification, and primary dependency docs; record evidence and unresolved questions.
**Decision / Selection rules:** compare native FastMCP mechanisms against custom alternatives before choosing; hand the result to architecture review.
**Version / Compatibility:** target FastMCP and MCP versions must be identified before research proceeds.

## Deliverables

**Deliverables / Artifacts:** a research record conforming to `contracts/research-contract.md`.
**Verification / Testing:** evidence ledger complete; unresolved questions recorded; sources and versions cited.
**Failure / Stop conditions:** stop rather than guess when official sources conflict, the target version is unclear, or behavior cannot be established from available evidence.
**Positive scenario:** a feature request is researched against current official docs before design and the research record is approved.
**Negative scenario:** implementation starts from memory; no evidence ledger exists; the target version is never pinned.
