# Exposure Detection Lab

This project explores templated vulnerability detection inspired by tools such as Nuclei.

The objective is to experiment with scalable exposure identification logic by:

- Detecting outdated services
- Identifying misconfigured web applications
- Parsing service banners
- Mapping service fingerprints to CVEs
- Testing signature-based detection workflows

---

## Research Goals

- Understand how agentless detection engines operate
- Build templated vulnerability checks
- Apply regex-based signature matching
- Automate HTTP probing and response parsing
- Explore exposure scoring logic (CVSS alignment)

---

## Architecture Overview

1. HTTP probe sends request
2. Response is parsed
3. Template matchers evaluate content
4. Detection logic flags potential exposure
5. Findings logged for review

---

## Example Detection Template

```yaml
id: outdated-nginx
info:
  severity: medium
  description: Detects outdated nginx versions vulnerable to known CVEs
requests:
  - method: GET
    path: /
    matchers:
      - type: regex
        pattern: "nginx/1.14.*"
