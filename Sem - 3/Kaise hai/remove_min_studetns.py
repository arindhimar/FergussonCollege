heights = [6, 2, 2, 8, 6, 1, 3, 2]

tempB = True
l = len(heights)
maxEle = max(heights)
lE = heights.index(maxEle)
print("Peak Index:", lE)

leftRemovals = 0
rightRemovals = 0

for i in range(1, lE + 1):
    if heights[i] <= heights[i - 1]:
        leftRemovals += 1  
for i in range(lE + 1, l):
    if heights[i] >= heights[i - 1]:
        rightRemovals += 1 
totalRemovals = leftRemovals + rightRemovals

if l - totalRemovals < 3 or leftRemovals == lE or rightRemovals == (l - lE - 1):
    print("NOT POSSIBLE")
else:
    print("Minimum to remove:", totalRemovals)
