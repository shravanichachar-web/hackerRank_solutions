from itertools import combinations_with_replacement

if __name__ == '__main__':
    # Read the string S and integer k from input
    user_input = input().split()
    S = user_input[0]
    k = int(user_input[1])
    
    # Sort the string to ensure combinations are generated in lexicographical order
    S = sorted(S)
    
    # Generate and print combinations with replacement
    for combo in combinations_with_replacement(S, k):
        print("".join(combo))
