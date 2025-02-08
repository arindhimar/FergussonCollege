class Engine:
    def __init__(self,horsepower):
        self.horsepower = horsepower
    
class Body:
    def __init__(self,material):
        self.material = material
        

class Car(Engine,Body):
    def __init__(self,horsepower,material):
        Engine.__init__(self,horsepower)
        Body.__init__(self,material)
    
    def show_details(self):
        print(self.horsepower,self.material)    
        

c = Car("780hp","StainLess Steel")
c.show_details()