class Employee:
    name=position=salary=""
    
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
        
    def display_info(self):
        print(self.name,self.position,self.salary)
        

e = Employee("arin","sde-1","2500000")

e.display_info()