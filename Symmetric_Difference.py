def main():
    # Read the size of the first set (we don't strictly need it in Python, but we must read the line)
    m = int(input())
    # Read the elements, map them to integers, and convert to a set
    a = set(map(int, input().split()))
    
    # Read the size of the second set
    n = int(input())
    # Read the elements, map them to integers, and convert to a set
    b = set(map(int, input().split()))
    
    # Calculate the symmetric difference using the built-in set method (or the ^ operator)
    sym_diff = a.symmetric_difference(b)
    
    # Sort the resulting set in ascending order and print each element on a new line
    for val in sorted(sym_diff):
        print(val)

if __name__ == '__main__':
    main()
