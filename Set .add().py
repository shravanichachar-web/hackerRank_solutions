# Read the number of stamps
n = int(input())

# Initialize an empty set to store distinct stamps
distinct_stamps = set()

# Loop n times to read each country and add it to the set
for _ in range(n):
    country = input().strip()
    distinct_stamps.add(country)
    
# Print the total number of distinct country stamps
print(len(distinct_stamps))
