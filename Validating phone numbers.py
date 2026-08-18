import re

# Read the number of test cases
n = int(input())

# Loop through each test case
for _ in range(n):
    # Read the input string
    s = input()
    
    # Check if it matches the valid mobile number pattern
    # ^       : Starts with
    # [789]   : Exactly one character which is 7, 8, or 9
    # \d{9}   : Exactly 9 digits (0-9)
    # $       : Ends right after those 9 digits (making it exactly 10 characters long)
    if re.match(r'^[789]\d{9}$', s):
        print("YES")
    else:
        print("NO")
