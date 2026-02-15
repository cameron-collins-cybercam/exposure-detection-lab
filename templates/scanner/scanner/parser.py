import re

def check_pattern(content, pattern):
    if re.search(pattern, content):
        return True
    return False
