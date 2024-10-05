class Engine:
    horsePower = 0
    def __init__(self):
        self.horsePower =450 
class Body:
    material =""
    def __init__(self) :
        self.material = "Carbon Fiber"
        
class Car(Engine,Body):
    def __init__(self):
        super().__init__()
        Body.__init__(self)
        
        
    def print_info(self):
        print(str(self.horsePower)+" "+self.material)
        

c = Car()
c.print_info()
