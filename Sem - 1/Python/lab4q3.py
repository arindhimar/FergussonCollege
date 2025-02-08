def unpackEmployeeData(tempTuple):
    (fname, lname, age, position, city) = tempTuple
    return fname, lname, age, position, city

def checkDeveloper(tempTuple):
    (_, _, _, position, _) = tempTuple
    return position == 'Developer'

employee_data = ('John', 'Doe', 34, 'Developer', 'New York')

fname, lname, age, position, city = unpackEmployeeData(employee_data)
print("Employee data:")
print(f"First name: {fname}")
print(f"Last name: {lname}")
print(f"Age: {age}")
print(f"Position: {position}")
print(f"City: {city}")

print(checkDeveloper(employee_data))

tempList = list(employee_data)

tempList.append('FullTime')

print(tempList)