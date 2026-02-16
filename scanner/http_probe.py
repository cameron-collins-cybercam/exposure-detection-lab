import requests
import os
import json
from parser import load_template, match_pattern

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "../templates")
TARGET_FILE = os.path.join(BASE_DIR, "../data/sample_targets.txt")

def fetch_url(url):
    try:
        response = requests.get(url, timeout=5)
        return return response.text, response.headers

    except Exception:
        return None

def load_targets():
    with open(TARGET_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def evaluate_templates(content):
    findings = []

    for filename in os.listdir(TEMPLATE_DIR):
        if not filename.endswith(".yaml"):
            continue

        template_path = os.path.join(TEMPLATE_DIR, filename)
        template = load_template(template_path)

        for request in template.get("requests", []):
            for matcher in request.get("matchers", []):
                pattern = matcher.get("pattern")
                if pattern and match_pattern(content, pattern):
                    findings.append({
                     "template_id": template.get("id"),
                     "severity": template.get("info", {}).get("severity"),
                     "description": template.get("info", {}).get("description"),
                     "cve": template.get("info", {}).get("cve"),
                     "cvss_score": template.get("info", {}).get("cvss_score")
                    })

    return findings

def main():
    targets = load_targets()

    for target in targets:
        print(f"\nScanning: {target}")
        
        server = headers.get("Server", "Unknown")
        print(f"  Server Banner: {server}")

        result = fetch_url(target)
        if not result:
            print("  Unable to fetch target.")
            continue
                    

        content, headers = result


        if not content:
            print("  Unable to fetch target.")
            continue

        findings = evaluate_templates(content)

        if findings:
            print("  Findings:")
            print(json.dumps(findings, indent=4))
        else:
            print("  No exposures detected.")

if __name__ == "__main__":
    main()
