def revString(str):
    revStr = ""
    for ch in str[::-1]:
        revStr+=ch
    print("Reverse String : ",revStr)
        
s = input("Enter String     ")
revString(s)