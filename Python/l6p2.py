class Employee:
    name , position , sal = "","",0
    
    def __init__(self):
        self.name = "Arin"
        self.position ="SDE-2"
        self.sal = 2500000
    def show_data(self):
        print("Name : "+self.name+" Position  : "+self.position+" Salary : "+str(self.sal))
        
e = Employee()
e.show_data()