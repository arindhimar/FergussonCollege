plainText="ashdahskdhaskhdkajksdh"

depth=3

enc={}

for i in range(depth):
    enc[i]=""
    
    
print(enc)

sign="+"

j=0



    
for i in range(len(plainText)):
    enc[j]+=plainText[i]
    if sign=="+":
        if j==depth-1:
            sign="-"
            j-=1
        else:
            j+=1
    else:
        if j==0:
            sign="+"
            j+=1
        else:
            j-=1
            

ee=""

for i in range(depth):
    ee+=enc[i]
    
    
print(ee)