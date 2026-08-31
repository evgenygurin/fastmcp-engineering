---
name: research-first
description: Enforce research-first workflow before any framework-sensitive change — use to prevent implementation based on stale APIs or assumptions.
---

# Research First

## Purpose

Prevent implementation based on memory, assumptions, stale APIs, or incomplete examples.

## Invocation

Use before any task that changes FastMCP behavior, MCP contracts, integrations, security, persistence, transport, lifecycle, or other framework-sensitive behavior.

## Required sequence

1. Clarify the requirement.
2. Identify versions.
3. Read official FastMCP documentation for the relevant feature and adjacent lifecycle/API sections.
4. Inspect relevant official FastMCP examples and tests.
5. Inspect the MCP specification for protocol semantics.
6. Read primary documentation for involved dependencies.
7. Compare native FastMCP mechanisms and custom alternatives.
8. Record evidence and unresolved questions.
9. Hand the result to architecture review.

## Deliverable

Create a research record conforming to `contracts/research-contract.md`.

## Stop conditions

Stop rather than guess when official sources conflict, the target version is unclear, or behavior cannot be established from available evidence.
