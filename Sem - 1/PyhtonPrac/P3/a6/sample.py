class Vehicle:
    brand=""
    
    def __init__(self,brand):
        self.brand = brand
    
    def printData(self):
        print(self.brand)
        
class Car(Vehicle):
    wheels=""
    def __init__(self,wheels,brand):
        # Vehicle.__init__(self,brand)
        super().__init__(brand)
        self.wheels = wheels
    
    def printData(self):
        Vehicle.printData(self)
        print(self.wheels)
        

c = Car("4","tempBrand")

c.printData()