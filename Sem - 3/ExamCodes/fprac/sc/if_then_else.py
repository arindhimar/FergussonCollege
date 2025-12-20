a = [[0.2], [0.6]]                
b = [[0.4, 0.9], [0.3, 0.5]]      

A = [row[0] for row in a]          
B = [val for row in b for val in row]   

lenA = len(A)
lenB = len(B)

cartesian = []

for i in range(lenA):
    row = []
    for j in range(lenB):
        row.append(min(A[i], B[j]))
    cartesian.append(row)

print(cartesian)
