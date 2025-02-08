def vowelCount(s):
    count =0
    for char in s:
        if char.lower()=="a" or char.lower()=="e" or char.lower()=="i" or char.lower()=="o" or char.lower()=="u":
            count+=1
    
    print(count)
    
    
vowelCount(input("Enter string "))