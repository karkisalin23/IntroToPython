# Creating a dictionary with various key-value pairs including a nested dictionary
my_dict = {
    'name': 'Salin',
    'age': 23,
    'city': 'Pittsburgh',
    'nestedDict': {'number': 15,
                   'coding': 'python'}
}

#Returns a view object that displays a list of all the keys in the dictionary.
keys = my_dict.keys()
print(keys)
print(type(keys))

#print the keys of the dictionary
print(list(my_dict.keys()))

#print the values of the dictionary
print(my_dict.values())

#print the (key, value) for all contents of the dictionary
print(my_dict.items())

#updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.
my_dict.update({'car': 'honda', 
                'color': 'black'})
print(my_dict)

#returns the value for the specified key if the key is in the dictionary, otherwise returns the default value.
value = my_dict.get('coding', "python")
print(value)