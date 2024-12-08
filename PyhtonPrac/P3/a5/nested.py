people = {
	'John': {'age': 45, 'city': 'New York'},
	'Mike': {'age': 22, 'city': 'Los Angeles'},
	'Sarah': {'age': 32, 'city': 'New York'},
	'Anna': {'age': 28, 'city': 'Chicago'}
}

for tempName in people:
    if people[tempName]['age']>30:
        print(tempName,people[tempName])