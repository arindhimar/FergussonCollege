class Animal:
    def speak(self):
        print("Animal Sound!!")
        

class Dog(Animal):
    def speak(self):
        print("Dog Sound!!")

class Cat(Animal):
    def speak(self):
        print("Cat Sound!!")
        
        

a = Animal()
a.speak()

d = Dog()
d.speak()

c = Cat()
c.speak()
    