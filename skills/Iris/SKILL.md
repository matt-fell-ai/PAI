# Iris Skill - Visual Debugging & Ingestion

| name | description |
| --- | --- |
| iris | Leverages Gemini 3.0 Pro's vision capabilities to analyze screenshots, videos, and PDFs for debugging and context ingestion. USE WHEN you need the AI to "see" a problem or extract structure from visual media. |

## The Key Insight
Images are data, not just art. **Iris** uses high-resolution multimodal processing to bridge the gap between "Pixels" and "Code." It can look at a UI bug, compare it to your CSS, and identify the exact line causing the shift.

## Usage

### Debug UI
```bash
pai run Iris debug "error_screenshot.png"
```

### Video Ingestion
```bash
pai run Iris watch "workflow_demo.mp4"
```

### PDF Structural Analysis
```bash
pai run Iris parse "complex_spec.pdf"
```

## How it Works
It utilizes the Gemini 3.0 `media_resolution` parameter to ingest high-fidelity visual data. It then runs a "Visual-to-Logic" loop that maps identified visual elements to your local repository files.

## Strategic Value
- **Zero-Friction Debugging**: Fix CSS and Layout issues in seconds.
- **Visual Onboarding**: Ingest complex documentation or whiteboard photos instantly.
- **Temporal Insight**: "Watch" a video of a system failing to identify the exact state transition where the error occurred.
