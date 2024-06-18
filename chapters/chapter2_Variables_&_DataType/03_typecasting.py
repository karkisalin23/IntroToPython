# Converting string to integer
num_str = "123"
num_int = int(num_str)
print(num_int)            # Output: 123
print(type(num_int))      # Output: <class 'int'>

# Converting integer to float
num_float = float(num_int)
print(num_float)          # Output: 123.0
print(type(num_float))    # Output: <class 'float'>

# Converting integer to string
num_str = str(num_int)
print(num_str)            # Output: "123"
print(type(num_str))      # Output: <class 'str'>

# Converting list to tuple
num_list = [1, 2, 3]
num_tuple = tuple(num_list)
print(num_tuple)          # Output: (1, 2, 3)
print(type(num_tuple))    # Output: <class 'tuple'>

# Converting tuple to list
num_list = list(num_tuple)
print(num_list)           # Output: [1, 2, 3]
print(type(num_list))     # Output: <class 'list'>

# Converting list to set
num_set = set(num_list)
print(num_set)            # Output: {1, 2, 3}
print(type(num_set))      # Output: <class 'set'>
