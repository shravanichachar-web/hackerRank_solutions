import re
import email.utils

# Read the number of test cases
n = int(input())

# Define the regex pattern for a valid email address
# ^[a-zA-Z]         : Must start with an English alphabetical character
# [a-zA-Z0-9_.-]*   : Subsequent characters can be alphanumeric, '_', '.', or '-'
# @                 : Must contain the '@' symbol
# [a-zA-Z]+         : Domain contains only English alphabetical characters
# \.                : Must contain a '.' separating domain and extension
# [a-zA-Z]{1,3}$    : Extension contains 1, 2, or 3 English alphabetical characters and ends the string
pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(n):
    # Read the full input string (e.g., "DEXTER <dexter@hotmail.com>")
    line = input()
    
    # Parse the name and email address into a tuple
    name, email_address = email.utils.parseaddr(line)
    
    # Check if the parsed email address exactly matches our regex pattern
    if re.match(pattern, email_address):
        # If valid, format it back into 'name <email>' and print
        print(email.utils.formataddr((name, email_address)))
