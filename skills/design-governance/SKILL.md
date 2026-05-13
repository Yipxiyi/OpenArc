---
name: design-governance
description: Use when creating or maintaining docs/DESIGN.md as the implementation-facing source of truth for UI, layout, component, accessibility, and interaction rules.
---

# Design Governance

Use this skill when a repository needs design-system guidance for implementation.

## Goal

Maintain `docs/DESIGN.md` as the source of truth for how UI should be built.

## Fixed Clarification Flow

If the user has not clearly specified design direction, follow this flow before writing:

1. Discover existing signals: app screens, CSS/theme files, component libraries, screenshots, assets, design docs, and product copy.
2. Extract confirmed patterns, gaps, contradictions, and risky assumptions.
3. Ask focused questions for material gaps such as audience, density, layout, typography, accessibility, and platform constraints.
4. Draft concrete implementation rules, not abstract taste statements.
5. Cross-check with `docs/PRD.md`, `docs/BRAND.md`, and `docs/assets/*`.
6. Confirm unresolved design decisions with the user.
7. Create or patch `docs/DESIGN.md`.

## DESIGN.md Owns

- Spacing
- Typography
- Tokens
- Layouts
- Interaction rules
- Responsive behavior
- Animation rules
- Accessibility
- Component standards
- Prohibited implementation patterns

## Boundary

Do not merge `docs/DESIGN.md` with `docs/BRAND.md`.

`DESIGN.md` governs UI implementation, engineering constraints, component systems, layout rules, and interaction behavior.

`BRAND.md` governs identity, storytelling, naming, tone, and communication style.

Cross-reference them when useful, but keep the source-of-truth boundary clear.

## Rules

- Detect an existing design system before writing defaults.
- Patch existing design docs instead of replacing them.
- Prefer concrete implementation rules over abstract taste statements.
- Reference `docs/assets/` when visuals, screenshots, or brand assets are needed.
- Do not invent a visual system when repository evidence and user intent are insufficient.
