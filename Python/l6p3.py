class Animal:
    def speak(self):
        print("Animal Speaks")


class Cat(Animal):
    def speak(self):
        print("Cat Meows")
        
class Dog(Animal):
    def speak(self):
        print("Dog Bhow Bhow")
        

c = Cat()
d = Dog()

c.speak()
d.speak()