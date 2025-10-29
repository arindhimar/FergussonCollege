nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 3
l = len(nums)
maxLen = 0

for i in range(l):
    tempK = 0
    tempL = 0
    for j in range(i, l):
        if nums[j] == 0:
            tempK += 1
        if tempK > k:
            break
        tempL += 1
        maxLen = max(maxLen, tempL)

print(maxLen)
