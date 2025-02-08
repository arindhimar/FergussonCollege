

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

temp = (1,'v1')

tempNew  = [(2,'banana'),(3,'apple'),(1,'orange')]

# n = 1 
# print([x[n] for x in tempNew])


tempNew.sort(key=lambda tup: tup[1]) 

print(tempNew)



