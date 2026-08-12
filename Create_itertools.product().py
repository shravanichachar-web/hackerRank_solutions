from itertools import product

def main():
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    result = list(product(A, B))
    
    print(*result)
    
if __name__ == '__main__':
    main()
