import re

# Read the input string
s = input()

# Search for the first occurrence of an alphanumeric character repeating consecutively
# ([a-zA-Z0-9]) captures a single alphanumeric character
# \1 matches the exact same character captured in the first group
match = re.search(r'([a-zA-Z0-9])\1', s)

# If a match is found, print the captured character; otherwise, print -1
if match:
    print(match.group(1))
else:
    print("-1")
