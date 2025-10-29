n=int(input("enter size"))

bottles= [1 ,2 ,3 ,4, 5] 
caps = [2, 2, 3, 1, 5]

count=0

for i in range(n):
    if caps[i]==bottles[i]:
        count+=1

print(count)