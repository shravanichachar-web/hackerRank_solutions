def average(array):
    
    distinct_heights = set(array)
    
    total_sum = sum(distinct_heights)
    
    count = len(distinct_heights)
    
    return total_sum / count
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
