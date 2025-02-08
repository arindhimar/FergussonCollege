tempDict = {
    "k1":"v1",
    "k2":"v2",
    "k3":"v3",
    "k4":"v4",
    "k5":"v5"
}

del tempDict["k4"]

print(tempDict)

# tempDict.popitem()
tempDict.pop("k5")


print(tempDict)
