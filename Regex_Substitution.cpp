import re

# Read the number of lines
n = int(input())

# Loop through each line of text
for _ in range(n):
    line = input()
    
    # (?<= ) is a positive lookbehind that ensures the match is preceded by a space
    # (&&|\|\|) matches exactly '&&' or '||'
    # (?= ) is a positive lookahead that ensures the match is followed by a space
    # The spaces are NOT consumed, which allows us to catch consecutive symbols like 'a && && b'
    
    modified_line = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda m: 'and' if m.group(0) == '&&' else 'or', line)
    
    print(modified_line)
