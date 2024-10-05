# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

# dog = Dog("Buddy", "Golden Retriever")
# print(dog.name)  
# print(dog.breed) 


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Mammal:
#     def __init__(self, hair_color):
#         self.hair_color = hair_color

# class Dog(Animal, Mammal):
#     def __init__(self, name, breed, hair_color):
#         Animal.__init__(self, name)
#         Mammal.__init__(self, hair_color)
#         self.breed = breed

# dog = Dog("Buddy", "Golden Retriever", "Golden")
# print(dog.name)  
# print(dog.breed) 
# print(dog.hair_color)


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Mammal(Animal):
#     def __init__(self, hair_color):
#         super().__init__("Mammal")
#         self.hair_color = hair_color

# class Dog(Mammal):
#     def __init__(self, breed, hair_color):
#         super().__init__(hair_color)
#         self.breed = breed

# dog = Dog("Golden Retriever", "Golden")
# print(dog.name)  
# print(dog.breed) 
# print(dog.hair_color)

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

class Cat(Animal):
    def __init__(self, breed):
        super().__init__("Cat")
        self.breed = breed

dog = Dog("Golden Retriever")
cat = Cat("Siamese")

print(dog.name)  
print(dog.breed) 

print(cat.name)  
print(cat.breed) 