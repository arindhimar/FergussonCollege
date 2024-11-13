class Car:
    brand=year=""
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    
    def displayInfo(self):
        print("Brand : "+ self.brand +" \nYear : "+ self.year)
        

carObj = Car("BMW","2004")

carObj.displayInfo()