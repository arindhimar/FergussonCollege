tempDict = {}

opt = True

while opt:
    
    strName = input("Enter name for mainKey")
    
    strAge = int(input("Enter age "))
    
    strCity = input("Enter city ")
    
    tempDict[strName] = {"age":strAge,"city":strCity}
    
    
        
    user_input = input("Enter 'False' to exit: ")
        
    if user_input == 'False':
        opt = False
        # print("Exiting the loop...")
        


for i in tempDict:
    if tempDict[i]['age']>30:
        print([i])
