import re

# Read the number of test cases
for _ in range(int(raw_input())):
    # Read the regex string
    s = raw_input()
    try:
        # Try to compile the regex
        re.compile(s)
        print True
    except re.error:
        # If an re.error is thrown, it is invalid
        print False
