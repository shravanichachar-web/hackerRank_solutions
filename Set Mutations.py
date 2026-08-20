# Read the number of elements in set A (we don't strictly need this value)
input()

# Read the elements of set A and convert them to a set of integers
A = set(map(int, input().split()))

# Read the number of operations we need to perform
N = int(input())

# Loop through each operation
for _ in range(N):
    # Read the operation name and the length of the other set
    # .split()[0] extracts just the command string (e.g., "update")
    command = input().split()[0]
    
    # Read the elements of the other set
    other_set = set(map(int, input().split()))
    
    # Apply the correct mutation operation based on the command
    if command == 'intersection_update':
        A.intersection_update(other_set)
    elif command == 'update':
        A.update(other_set)
    elif command == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)
    elif command == 'difference_update':
        A.difference_update(other_set)

# Print the sum of the elements remaining in set A
print(sum(A))
