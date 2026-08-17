from itertools import product

if __name__ == '__main__':
    # Read K (number of lists) and M (modulo value)
    K, M = map(int, input().split())
    
    lists = []
    for _ in range(K):
        # Read each line, skip the first element (which is the count)
        data = list(map(int, input().split()))[1:]
        
        # Optimization: Square each number and apply modulo M immediately.
        # This keeps the numbers small and avoids redundant large multiplications later.
        squared_modulo_list = [(x**2) % M for x in data]
        lists.append(squared_modulo_list)
    
    # itertools.product generates all possible combinations picking one element from each list.
    # We find the sum of each combination, apply modulo M, and take the maximum.
    max_value = max(sum(combo) % M for combo in product(*lists))
    
    print(max_value)
