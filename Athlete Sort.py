if __name__ == '__main__':
    # Read the number of athletes (N) and attributes (M)
    n, m = map(int, input().split())
    
    # Initialize a list to hold all the athlete data
    athletes = []
    
    # Read the data for each athlete
    for _ in range(n):
        row = list(map(int, input().split()))
        athletes.append(row)
        
    # Read the attribute index (K) to sort by
    k = int(input())
    
    # Sort the athletes list based on the K-th attribute.
    # Python's .sort() is stable, so equal values remain in their original input order.
    athletes.sort(key=lambda x: x[k])
    
    # Print the sorted rows
    for row in athletes:
        # The unpacking operator (*) prints the list elements separated by spaces
        print(*row)
