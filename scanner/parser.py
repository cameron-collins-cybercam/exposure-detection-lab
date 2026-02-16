import re
import yaml

def load_template(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def match_pattern(content, pattern):
    return re.search(pattern, content) is not None
