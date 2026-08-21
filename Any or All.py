_, nums = input(), input().split()
print(all(int(i) > 0 for i in nums) and any(j == j[::-1] for j in nums))
