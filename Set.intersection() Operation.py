if __name__ == '__main__':
    # Read the number of English newspaper subscribers (we don't actually need to use this variable)
    n = int(input())
    # Read the roll numbers and store them in a set
    english_subs = set(input().split())
    
    # Read the number of French newspaper subscribers
    b = int(input())
    # Read the roll numbers and store them in a set
    french_subs = set(input().split())
    
    # Get the intersection of both sets (students subscribed to both)
    both_subs = english_subs.intersection(french_subs)
    
    # Print the total number of students in the intersection
    print(len(both_subs))
