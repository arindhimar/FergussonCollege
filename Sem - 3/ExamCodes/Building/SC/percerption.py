threshold=1.5
inputs = [1, 0, 1, 0, 1]
weights = [0.7, 0.6, 0.5, 0.3, 0.4]

s=0

for i in range(len(inputs)):
    s+=inputs[i]*weights[i]

print(s>threshold)