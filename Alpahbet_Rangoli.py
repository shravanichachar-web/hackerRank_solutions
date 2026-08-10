import string
def print_rangoli(size):
    
    alpha = string.ascii_lowercase
    lines = []
    
    width = 4 * size - 3
    
    for i in range(size):
        
        s = alpha[size - 1 - i : size]
        
        row = "-".join(s[::-1] + s[1:])
        
        lines.append(row.center(width, "-"))
        
    result = "\n".join(lines + lines[:-1][::-1])
    
    print(result) 
    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
