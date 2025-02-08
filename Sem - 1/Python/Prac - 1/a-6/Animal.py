class Animal:
    def speak(self):
        print("Animal speaks!!")
        

class Dog(Animal):
    def speak(self):
        print("Dog barks!!")
        
dogObj = Dog()
dogObj.speak()