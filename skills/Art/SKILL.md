---
name: Art
description: Complete visual content system for PAI. Tron-meets-Excalidraw aesthetic. USE WHEN user wants to create visual content, illustrations, diagrams, or visualizations.
---

# Art Skill

Complete visual content system using the **PAI Visual Aesthetic**.

## Workflow Routing

| Workflow | Trigger | File |
|----------|---------|------|
| **Visualize** | "visualize this", "create diagram" | `workflows/Visualize.md` |
| **Workflow** | "blog header", "editorial" | `workflows/Workflow.md` |
| **Mermaid** | "flowchart", "sequence diagram" | `workflows/Mermaid.md` |

## Examples

**Example 1: Create a technical diagram**
```
User: "Visualize the PAI hook system"
→ Invokes Visualize workflow
→ Decomposes system into nodes
→ Generates PAI-aesthetic diagram
```

---

**Full aesthetic documentation:** `${PAI_DIR}/skills/CORE/Aesthetic.md`
