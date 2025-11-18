def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

def main():
    P = 23
    G = 9

    a = 4
    

    x = power(G, a, P)

    b = 3
    

    y = power(G, b, P)

    ka = power(y, a, P)  
    kb = power(x, b, P) 

    print( ka)
    print(kb)
    
    
main()