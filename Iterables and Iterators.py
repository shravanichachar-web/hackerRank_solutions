from itertools import combinations

if __name__ == '__main__':
    # Read inputs
    N = int(input())
    letters = input().split()
    K = int(input())
    
    # Generate all possible combinations of length K
    all_combinations = list(combinations(letters, K))
    
    # Count how many combinations contain at least one 'a'
    valid_combinations = sum(1 for combo in all_combinations if 'a' in combo)
    
    # Calculate and print the probability
    probability = valid_combinations / len(all_combinations)
    
    # Print the probability rounded to 4 decimal places to match sample output
    print(round(probability, 4))
