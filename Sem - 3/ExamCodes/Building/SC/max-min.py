# # Input dimensions
# r1 = int(input("Enter rows for L1: "))
# c1 = int(input("Enter columns for L1: "))
# r2 = int(input("Enter rows for L2: "))
# c2 = int(input("Enter columns for L2: "))

# print("Enter elements for L1 (0-1 as fuzzy values):")
# l1 = [[float(input()) for _ in range(c1)] for _ in range(r1)]

# print("Enter elements for L2 (0-1 as fuzzy values):")
# l2 = [[float(input()) for _ in range(c2)] for _ in range(r2)]


r1, c1 = 2, 3
r2, c2 = 3, 2

l1 = [
    [0.2, 0.5, 0.8],
    [0.4, 0.6, 0.9]
]

l2 = [
    [0.3, 0.7],
    [0.5, 0.2],
    [0.9, 0.4]
]


maxMin=[]

for i in range(r1):
    row=[]
    for j in range(c2):
        temp=[]
        for k in range(c1):
            temp.append(min(l1[i][k], l2[k][j]))
        row.append(max(temp))
    maxMin.append(row)
    
    
print(maxMin)