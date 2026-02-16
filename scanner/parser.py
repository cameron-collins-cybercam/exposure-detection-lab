import re
import yaml

def load_template(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def check_pattern(content, pattern):
    if re.search(pattern, content):
        return True
    return False
