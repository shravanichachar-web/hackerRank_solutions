import re

# Read the input string
s = input()

# Define the vowels and consonants explicitly as requested by the problem
vowels = "AEIOUaeiou"
consonants = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"

# Build the regex pattern using positive lookbehind (?<=...) and positive lookahead (?=...)
# This ensures we don't consume the consonants when finding matches, 
# which is important for overlapping boundaries (e.g., 'baabioob' sharing the 'b').
pattern = r"(?<=[{c}])([{v}]{{2,}})(?=[{c}])".format(c=consonants, v=vowels)

# Find all matches
matches = re.findall(pattern, s)

# Print the results
if matches:
    print("\n".join(matches))
else:
    print("-1")
