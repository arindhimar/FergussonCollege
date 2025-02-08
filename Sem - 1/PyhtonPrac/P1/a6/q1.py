class Car:
    brand=year=""
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    
    def display_info(self):
        print(self.brand,self.year)

    
    
c = Car("BMW","2003")
c.display_info()