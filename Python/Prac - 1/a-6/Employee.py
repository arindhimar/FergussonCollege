class Employee:
    name=position=salary=""
    def __init__(self,v1,v2,v3):
        self.name=v1
        self.position=v2
        self.salary=v3
    
    def printData(self):
        print(self.name,self.position,self.salary)
        
empObj = Employee("Arin","Project Manager","1000000")
empObj.printData()