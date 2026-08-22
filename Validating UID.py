def is_valid_uid(uid):
    # Rule 5: Exactly 10 characters
    if len(uid) != 10:
        return False
    
    # Rule 3: Only alphanumeric characters
    if not uid.isalnum():
        return False
        
    # Rule 4: No character should repeat
    if len(set(uid)) != len(uid):
        return False
        
    # Rule 1 & 2: At least 2 uppercase and at least 3 digits
    upper_count = sum(1 for char in uid if char.isupper())
    digit_count = sum(1 for char in uid if char.isdigit())
    
    if upper_count < 2 or digit_count < 3:
        return False
        
    return True

if __name__ == '__main__':
    # Read the number of test cases
    t = int(input())
    
    # Process each UID
    for _ in range(t):
        uid = input().strip()
        if is_valid_uid(uid):
            print("Valid")
        else:
            print("Invalid")
