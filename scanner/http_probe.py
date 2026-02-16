import requests
import os
from parser import load_template, check_pattern

TEMPLATE_DIR = "../templates"

def fetch_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def evaluate_templates(content):
    for file in os.listdir(TEMPLATE_DIR):
        template_path = os.path.join(TEMPLATE_DIR, file)
        template = load_template(template_path)

        for request in template.get("requests", []):
            for matcher in request.get("matchers", []):
                pattern = matcher.get("pattern")
                if pattern and check_pattern(content, pattern):
                    print(f"[!] Potential Match: {template['id']}")
                    print(f"    Severity: {template['info']['severity']}")
                    print(f"    Description: {template['info']['description']}")

if __name__ == "__main__":
    url = "http://example.com"
    content = fetch_url(url)
    if content:
        evaluate_templates(content)
