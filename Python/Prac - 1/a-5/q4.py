people = {
	'John': {'age': 45, 'city': 'New York'},
	'Mike': {'age': 22, 'city': 'Los Angeles'},
	'Sarah': {'age': 32, 'city': 'New York'},
	'Anna': {'age': 28, 'city': 'Chicago'}
}



lst = [ i for i in people if people[i]['age']>30 and people[i]['city'] == 'New York']

print(lst)