height = float(input("Enter height (in metrers)"))
weight = float(input("Enter weight (in kg)"))

bmi = (weight/(height**2))

print("BMI index of user with ",height,"meters and ",weight," kg is ",bmi)

if bmi>18.5 and bmi<25:
    print("Normal")
elif bmi<=18.5:
    print("Under Weight")
else:
    print("OverWeight")