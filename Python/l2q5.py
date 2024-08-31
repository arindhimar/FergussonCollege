def greet(name,msg="Hello"):
    print(msg,name)
    

name = input("Enter Name ")
msg = input("Enter Message ")

if len(msg)== 0:
    greet(name)
else:
    greet(name,msg)
