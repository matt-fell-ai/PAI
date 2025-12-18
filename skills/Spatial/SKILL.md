# Spatial Skill - Architectural Blueprinting

| name | description |
| --- | --- |
| spatial | Maps visual sketches and diagrams directly to project infrastructure and code. USE WHEN you have a whiteboard photo, a hand-drawn diagram, or a digital mock-up. |

## The Key Insight
Ideas are born as sketches. **Spatial** is the translator between "Visual Design" and "Technical Execution." It turns a drawing of a database schema into actual SQL migrations and UFC folders.

## Usage

### Blueprint Diagram
```bash
pai run Spatial blueprint "schema_sketch.jpg"
```

### Map UI
```bash
pai run Spatial map "figma_export.png"
```

## How it Works
It coordinates with the `Visionary` and `UFC` skills. It uses Gemini 3.0's high-fidelity vision to extract nodes and relationships from an image and then calls `Blueprint` to instantiate the structure.

## Strategic Value
- **Diagram-to-Done**: Skip the manual translation of your whiteboard notes.
- **Architectural Clarity**: Forces you to visualize your system before building.
- **Unified Design**: Ensures that what you "imagined" is exactly what the PAI "builds."
