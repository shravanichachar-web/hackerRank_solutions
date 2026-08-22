import re

def is_valid_float(s):
    # The regex pattern enforces all the specific rules of the problem
    pattern = r'^[-+]?[0-9]*\.[0-9]+$'
    return bool(re.match(pattern, s))

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input().strip())
    
    # Process each test case
    for _ in range(t):
        s = input()
        print(is_valid_float(s))
