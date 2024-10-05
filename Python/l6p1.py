class Car:
    brand ,name ="",""
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        
        
    def display_info(self):
        print("Brand : "+self.brand+" Name : "+self.name)
        


p = Car("a","a")
p.display_info()
p.color = "a"
print("Color : "+p.color)