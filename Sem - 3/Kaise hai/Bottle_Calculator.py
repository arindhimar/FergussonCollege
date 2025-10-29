n=5

bottles= ["1b" ,"2b" ,"3b" ,"4b", "5b"] 

caps = ["2c", "2c", "3c", "1c", "5c"]


count=0

for i in range(n):
    tempC=[c for c in caps[i]]
    tempB=[c for c in bottles[i]]
    if tempC[0]==tempB[0]:
        count+=1

print(count)