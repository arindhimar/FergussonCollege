def print_details(**d):
    for key,val in d.items():
        print(key," - >",val)

b = True
l = {}
while b:
    
    key = input("Enter key")
    value = input("Enter value")
    l[key] = value
    b = input("Enter False to exit: ").lower() != 'false'

print_details(**l)