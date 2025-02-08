student_grades = {'Ram': 85, 'Sham': 92, 'Ojas’': 88, 'Anay': 79}

# print(sorted(student_grades.items(),key = lambda x : x[1],reverse=True)[0])

def unpk(*tempEmp):
    fname,lname,age,pos,loc = tempEmp
    # return fname,lname,age,pos,loc
    return pos == 'Developer'

employee_data = ('John', 'Doe', 34, 'Developer', 'New York')



# print(unpk(*employee_data))

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# print(list(map(lambda x,y:x**y,list1,list2)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x:x%2==0,numbers)))
