# Librarian Skill - Semantic Memory & Knowledge Retrieval

| name | description |
| --- | --- |
| librarian | Deep search and retrieval across the entire PAI knowledge base (History, Skills, Memory). USE WHEN you need to find past solutions, conceptually related code, or project context. |

## The Key Insight
History is useless if you can't find the right moment. **Librarian** provides a "Search Layer" above raw files. It understands that "OAuth" and "Authentication" are related, ensuring you never rebuild a wheel you've already perfected.

## Usage

### Concept Search
```bash
pai run Librarian search "How do I handle state?"
```

### Context Retrieval
```bash
pai run Librarian context "project-x"
```

## How it Works
It builds a local index of the `History/` system. It utilizes `ripgrep` (if available) or Python's `os.walk` with weighted keyword matching to find the most relevant files across different subdirectories (Sessions, Learnings, Execution).

## Strategic Value
- **Zero-Waste Development**: Instantly find how you solved a similar problem 3 months ago.
- **Onboarding**: Quickly get up to speed on a project's history by searching for the "Story".
- **Concept Linking**: Automatically links new tasks to past relevant decisions.
