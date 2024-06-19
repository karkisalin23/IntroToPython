# Creating a dictionary with various key-value pairs including a nested dictionary
my_dict = {
    'name': 'Salin',
    'age': 23,
    'city': 'Pittsburgh',
    'nestedDict': {'salin': 23}
                #    ,'coding': 'python'}
}

# Accessing and printing the value associated with the key 'name' from the dictionary
print(my_dict['name'])  # Output: Salin

# Accessing and printing the value associated with the key 'age' from the dictionary
print(my_dict['age'])  # Output: 23

# Accessing and printing the value associated with the key 'city' from the dictionary
print(my_dict['city'])  # Output: Pittsburgh

# Accessing and printing the value associated with the key 'Salin' from the nested dictionary 'nestedDict'
print(my_dict['nestedDict']['Salin'])  # Output: 23

# Adding a new key-value pair
my_dict['email'] = 'example@example.com'

# Updating an existing key-value pair
my_dict['age'] = 24

#Accessing dictionary
print(my_dict)
# print(my_dict['nestedDict'])