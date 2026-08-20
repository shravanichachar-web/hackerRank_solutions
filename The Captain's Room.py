# Read the size of each group
k = int(input())

# Read the room numbers into a list of integers
rooms = list(map(int, input().split()))

# Calculate the sums
unique_rooms_sum = sum(set(rooms))
total_rooms_sum = sum(rooms)

# Use the mathematical difference to find the Captain's room
captain_room = (unique_rooms_sum * k - total_rooms_sum) // (k - 1)

# Print the Captain's room number
print(captain_room)
