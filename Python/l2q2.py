def countVowel(s=""):
    count = 0
    for ch in s:
        if ch.lower()=='a' or ch.lower()=='e' or ch.lower()=='i' or ch.lower()=='o' or ch.lower()=='u':
            count+=1
    print("Count of vowel : ",count)

str = input("Enter string ")

countVowel(str)