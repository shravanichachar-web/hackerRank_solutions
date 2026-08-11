import cmath 

if __name__ == '__main__':
    
    z = complex(input().strip())
    
    r = abs(z)
    
    phi = cmath.phase(z)
    
    print(r)
    print(phi)
