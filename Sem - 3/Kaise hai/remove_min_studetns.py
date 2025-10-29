heights = [6, 2, 2, 8, 6, 1, 3, 2]

original = heights[:]  
removed_indices = []

n = len(heights)
maxEle = max(heights)
idx = heights.index(maxEle)

i = 1
while i < idx:
    if heights[i - 1] >= heights[i]:
        removed_indices.append(original.index(heights[i]))
        heights.pop(i)
        idx -= 1
        n -= 1
        # don't increment i here
    else:
        i += 1

i = idx + 1
while i < len(heights):
    if heights[i - 1] <= heights[i]:
        removed_indices.append(original.index(heights[i]))
        heights.pop(i)
        n -= 1
        # don't increment i here
    else:
        i += 1

if len(heights) < 3 or idx == 0 or idx == len(heights) - 1:
    print("NOT POSSIBLE")
else:
    print("Remaining mountain:", heights)
    print("Students removed:", len(original) - len(heights))
    print("Indices removed:", sorted(set(removed_indices)))
