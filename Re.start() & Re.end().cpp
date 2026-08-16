import re

# Read the strings S and k
S = input()
k = input()

# Compile the pattern for efficient searching
# We treat string k as the regular expression pattern
pattern = re.compile(k)

# Find the first match
m = pattern.search(S)

# If no match is found, print the default failure tuple
if not m:
    print("(-1, -1)")
else:
    # Loop to find all overlapping matches
    while m:
        # m.start() returns the starting index of the match
        # m.end() returns the index immediately AFTER the match, so we subtract 1
        print(f"({m.start()}, {m.end() - 1})")
        
        # Search again starting from the index immediately after the current match's start 
        # This allows us to catch overlapping substrings (e.g., 'aa' inside 'aaadaa')
        m = pattern.search(S, m.start() + 1)
