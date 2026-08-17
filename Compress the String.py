from itertools import groupby

if __name__ == '__main__':
    # Read the input string
    S = input()
    
    # Use groupby to group identical consecutive characters
    # Calculate the length of the group and convert the character to an integer
    compressed = [(len(list(g)), int(k)) for k, g in groupby(S)]
    
    # Unpack the list using * to print the tuples separated by a space
    print(*compressed)
