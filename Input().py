# Read x and k from the first line
x, k = map(int, input().split())

# Read the polynomial expression from the second line
polynomial = input()

# eval() evaluates the string expression mathematically.
# Because we already have a variable named 'x' defined above, 
# eval() will automatically substitute its value into the polynomial.
if eval(polynomial) == k:
    print(True)
else:
    print(False)
