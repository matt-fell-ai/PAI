# Fold Skill

## Overview
`Fold` implements Recursive Context Compression for the PAI. It prevents "Context Saturation" during long-horizon projects by folding history into strategic summaries.

## Strategic Purpose
To maintain 100% reasoning accuracy during complex tasks by keeping the working context 10x smaller while retaining mission-critical insights.

## Tools
- `compress <log_file>`: Folds a large log file into a strategic summary.
- `archive`: Prunes non-essential context from the current session.
- `restore`: Unfolds a summary back into detailed context (Lossless reconstruction).

## Use When
- You are 10+ turns into a complex coding or research session.
- Managing multi-day agent swarms via `Hive`.
- Optimizing PAI performance for long-horizon planning.
