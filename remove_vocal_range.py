#!/usr/bin/env python3
"""
Remove vocal range indicators from theory badges
"""

with open('index.html', 'r') as f:
    html = f.read()

# Remove the vocal range portion (everything after the last |)
# Pattern: theory: 'KEY | PROGRESSION | EMOJI High: NOTE'
# Want: theory: 'KEY | PROGRESSION'

import re

# Find all theory fields and remove the vocal range part
pattern = r"(theory: '[^']+?) \| [✅👍⚠️❌] High: [A-G]#?[0-9]'"
replacement = r"\1'"

html = re.sub(pattern, replacement, html)

with open('index.html', 'w') as f:
    f.write(html)

print("✅ Removed all vocal range indicators from theory badges")
print("Theory badges now show only music theory information")
