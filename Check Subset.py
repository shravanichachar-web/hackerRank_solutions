# Read the number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the number of elements in set A (we don't actually need to store this)
    input()
    
    # Read the elements of set A
    A = set(input().split())
    
    # Read the number of elements in set B (we don't actually need to store this)
    input()
    
    # Read the elements of set B
    B = set(input().split())
    
    # Check if A is a subset of B and print the boolean result
    print(A.issubset(B))
