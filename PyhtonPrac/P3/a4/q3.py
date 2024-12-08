def unpk(*tempData):
    name,fname,age,pos,loc = tempData
    return name,fname,age,pos,loc 
def ck(*tempData):
    name,fname,age,pos,loc = tempData
    return pos =='Developer'



employee_data = ('John', 'Doe', 34, 'Developer', 'New York')


print(ck(*employee_data))

temp = list(employee_data)
temp.append('Fill TImw')

print(temp)