import numpy as np

# Read the dimensions of the arrays (N rows, M columns)
n, m = map(int, input().split())

# Read the next N lines to form array A, ensuring the type is integer
A = np.array([input().split() for _ in range(n)], int)

# Read the following N lines to form array B, ensuring the type is integer
B = np.array([input().split() for _ in range(n)], int)

# Perform and print the element-wise mathematical operations
print(A + B)       # Addition
print(A - B)       # Subtraction
print(A * B)       # Multiplication
print(A // B)      # Integer Division (using // as instructed for Python 3)
print(A % B)       # Modulo
print(A ** B)      # Power
