def countVowel(st):
    count=0
    for ch in st:
        if(ch.lower()=="a" or ch.lower()=="e" or ch.lower()=="i" or ch.lower()=="o" or ch.lower()=="u"):
            count+=1
    
    print("Count of vowels : "+str(count))
        
        
countVowel("Arin is the absolute best of all")