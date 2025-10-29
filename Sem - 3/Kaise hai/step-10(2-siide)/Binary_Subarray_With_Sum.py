nums = [1, 0, 0, 1, 1, 0]
goal = 2
count = 0
n = len(nums)

for i in range(n):
    tempS = 0
    for j in range(i, n):
        tempS += nums[j]
        if tempS > goal:
            break
        if tempS == goal:
            count += 1

print("Total count:", count)
