class Vehicle:
    brand=speed=""
    
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
        
    def show_details(self):
        print(self.brand,self.speed)
        

class Car(Vehicle):
    mileage = ""
    
    def __init__(self,brand,speed,mileage):
        super().__init__(brand,speed)
        self.mileage = mileage
        
    def show_details(self):
        super().show_details()
        print(self.mileage)
        
c = Car("brand","speed","mileage")

c.show_details()