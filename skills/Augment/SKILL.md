# Augment Skill - The API-ification Layer

| name | description |
| --- | --- |
| augment | Transforms static websites and data sources into personal APIs and CLI tools. USE WHEN you need to extract structured data from a source that doesn't have an official API. |

## The Key Insight
Turn the world into an API. **Augment** allows you to "wrap" any URL or data stream into a CLI tool. Instead of browsing a site, you "pipe" the site into your PAI. It automates the extraction and transformation of unstructured data into your `UFC` Knowledge base.

## Usage

### Create API Wrapper
```bash
pai run Augment api --url "https://news.ycombinator.com"
```

### Data Stream
```bash
pai run Augment stream "GitHub Repo Activity"
```

## How it Works
It coordinates with the `Fabric` and `Research` skills. It fetches the raw content, generates a temporary Python parsing script, and returns the result as a structured JSON object.

## Strategic Value
- **Information Mastery**: Access data on your own terms, not the website's.
- **Automation Base**: Once a site is an "API," it can be used by `Alpha` or `Shadow` for background monitoring.
- **Workflow Speed**: Zero-friction data ingestion for your daily projects.
