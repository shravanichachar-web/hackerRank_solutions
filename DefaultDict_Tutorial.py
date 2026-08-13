from collections import defaultdict

def main():
    n, m = map(int, input().split())
    
    d = defaultdict(list)
    
    for i in range(1, n + 1):
        word = input().strip()
        
        d[word].append(str(i))
        
    for _ in range(m):
        word = input().strip()
        
        if word in d:
            print(" ".join(d[word]))
        else:
            print("-1")
            
if __name__ == '__main__':
    main()
