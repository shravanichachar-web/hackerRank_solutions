from itertools import permutations

if __name__ == '__main__':
    # Read the input line and unpack it directly into s and k
    s, k = input().split()
    
    # Sort the string, get permutations of length int(k), and print
    for p in permutations(sorted(s), int(k)):
        print("".join(p))
