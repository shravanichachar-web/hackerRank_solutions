# The lambda function to cube a number
cube = lambda x: x ** 3

def fibonacci(n):
    # Initialize an empty list to store the sequence
    fib_list = []
    
    # Starting values for the Fibonacci sequence
    a, b = 0, 1
    
    # Loop 'n' times to generate the first 'n' numbers
    for _ in range(n):
        fib_list.append(a)
        # Update values: 'a' becomes 'b', and 'b' becomes the sum of both
        a, b = b, a + b
        
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
