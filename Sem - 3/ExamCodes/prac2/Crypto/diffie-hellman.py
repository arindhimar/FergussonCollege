def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

def main():
    #prime
    P = 23
    #primitve number
    G = 9

    #user a seleted this
    a = 4
    x = power(G, a, P)

    #user b seleted this
    b = 3
    y = power(G, b, P)

    ka = power(y, a, P)  
    kb = power(x, b, P) 

    print(ka)
    print(kb)
    
    
main()