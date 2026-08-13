def main():
    # Read the size of the first set (we don't strictly need to use this variable)
    m = int(input())
    # Read the elements, split them by space, convert to integers, and create a set
    set_a = set(map(int, input().split()))
    
    # Read the size of the second set
    n = int(input())
    # Read the elements for the second set
    set_b = set(map(int, input().split()))
    
    # Calculate the symmetric difference
    # Python sets have a built-in method for this, or you can use the ^ operator
    sym_diff = set_a.symmetric_difference(set_b)
    
    # Sort the resulting set in ascending order and print each element on a new line
    for val in sorted(sym_diff):
        print(val)

if __name__ == '__main__':
    main()
