class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def showData(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}")

class Car(Vehicle):
    def __init__(self, mileage, brand, speed):
        super().__init__(brand, speed)  
        self.mileage = mileage
    
    def showData(self):
        super().showData()  
        print(f"Mileage: {self.mileage}")

# Create an instance of Car
carObj = Car("10 km/l", "BMW", "240 km/h")
carObj.showData()