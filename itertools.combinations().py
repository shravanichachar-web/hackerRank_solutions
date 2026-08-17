from itertools import combinations

if __name__ == '__main__':
    # Read the string S and the integer k from input
    user_input = input().split()
    S = user_input[0]
    k = int(user_input[1])
    
    # Sort the string first so the combinations are emitted in lexicographical order
    S = sorted(S)
    
    # Loop from length 1 up to k
    for i in range(1, k + 1):
        # Generate and print combinations of the current length
        for combo in combinations(S, i):
            print("".join(combo))
