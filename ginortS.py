# Read the input string
s = input()

# Sort the string with a custom key
# The key creates a tuple for each character. Python sorts tuples element by element.
# 1. c.isdigit() -> False (0) for letters, True (1) for digits. (Puts letters before digits)
# 2. c.isdigit() and int(c) % 2 == 0 -> True (1) for even digits, False (0) for others. (Puts odd digits before even digits)
# 3. c.isupper() -> False (0) for lowercase, True (1) for uppercase. (Puts lowercase before uppercase)
# 4. c -> Finally, sorts alphabetically/numerically within each specific group.
sorted_s = sorted(s, key=lambda c: (c.isdigit(), c.isdigit() and int(c) % 2 == 0, c.isupper(), c))

# Join the sorted list of characters back into a string and print it
print("".join(sorted_s))
