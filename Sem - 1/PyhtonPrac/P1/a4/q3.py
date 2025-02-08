def unpk(*tempTuple):
    v1,v2,v3,v4,v5 = tempTuple
    return v1,v2,v3,v4,v5


def checkDev(*tempTuple):
    _,_,_,v4,_ = tempTuple
    return v4 == 'Developer'


employee_data = ('John', 'Doe', 34, 'Developer', 'New York')
print(unpk(*employee_data))
print(checkDev(*employee_data))