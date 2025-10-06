n = int(input("Enter a prime number (n): "))
g = int(input("Enter a primitive root (g): "))

x = int(input("A's private key (x): "))
A = pow(g, x, n)   # A = g^x mod n

y = int(input("B's private key (y): "))
B = pow(g, y, n)  

print("\nPublicly exchanged values:")
print("A sends A =", A)
print("B sends B =", B)

KA = pow(B, x, n)  # A's computes key
KB = pow(A, y, n)

print("\nShared Secret Keys:")
print("A's computed key:", KA)
print("B's computed key:  ", KB)

if KA == KB:
    print("\n✅ Key exchange successful! Shared Key =", KA)
else:
    print("\n❌ Key exchange failed!")
