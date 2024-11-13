def checkDeveloper(*empData):
    if('Developer' in empData):
        lst = list(empData)
        lst.append("Full Time")
        print(lst)


employee_data = ('John', 'Doe', 34, 'Developer', 'New York')

checkDeveloper(*employee_data)
