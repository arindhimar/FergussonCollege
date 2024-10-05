class Vehicle :
    brand,speed ="Brand",100
    
    def show_details(self):
        print("Brand :"+self.brand+" Speed : "+str(self.speed))
        
    
class Car(Vehicle):
    mileage=24
    
    def show_details(self):
        print("Mileage : "+str(self.mileage))
        return super().show_details()
    
    
c = Car()
c.show_details()