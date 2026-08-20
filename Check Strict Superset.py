# Read the space-separated elements of set A
A = set(input().split())

# Read the number of other sets
n = int(input())

# Assume A is a strict superset until proven otherwise
is_strict_superset = True

# Loop through each of the n sets
for _ in range(n):
    # Read the elements of the current other set
    other_set = set(input().split())
    
    # Check if A is a strict superset of this other_set using the '>' operator
    if not (A > other_set):
        is_strict_superset = False
        break  # We can stop checking as soon as one fails

# Print the final boolean result
print(is_strict_superset)
