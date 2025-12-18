# Guardian Skill - Quality & Security

| name | description |
| --- | --- |
| guardian | Automated security, linting, and alignment checks. USE WHEN you want to verify the health of the repository or ensure new code follows the PAI architecture. |

## The Key Insight
Entropy is the enemy of infrastructure. **Guardian** ensures that the system stays clean, secure, and aligned with its core principles (as defined in `CORE/CONSTITUTION.md`).

## Usage

### Check Repo Health
```bash
pai run Guardian check
```

### Validate Style
```bash
pai run Guardian lint
```

### Security Scan
```bash
pai run Guardian secure
```

## How it Works
It runs a battery of tests, including `git status` checks, `lint` tools (if available), and custom regex-based scans to find secrets or non-compliant patterns (e.g., hardcoded paths instead of `${PAI_DIR}`).

## Strategic Value
- **DevSecOps for One**: Brings enterprise-grade security checks to your personal setup.
- **Architectural Integrity**: Prevents "feature creep" and "code rot".
- **Safety First**: Catch sensitive data leaks before they are committed to GitHub.
