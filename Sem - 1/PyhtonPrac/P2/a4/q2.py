def unpackEmp(tempData):
    fname,lname,age,pos,city = tempData
    return fname,lname,age,pos,city 

def checkDeveloper(tempData):
    _,_,_,pos,_ = tempData
    return pos =='Developer'

employee_data = ('John', 'Doe', 34, 'Developer', 'New York')

print(checkDeveloper(employee_data))

print(unpackEmp(employee_data))

employee_list = list(employee_data)
employee_list.append('Full-time')

print(employee_list)