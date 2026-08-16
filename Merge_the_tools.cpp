def merge_the_tools(string, k):
    # Iterate through the string with a step size of k
    for i in range(0, len(string), k):
        # Slice the string to get a substring of length k
        substring = string[i:i+k]
        
        # dict.fromkeys() creates a dictionary with the characters as keys.
        # Since dictionaries in modern Python/PyPy maintain insertion order, 
        # this perfectly removes duplicates while keeping the original order.
        unique_substring = "".join(dict.fromkeys(substring))
        
        print(unique_substring)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
