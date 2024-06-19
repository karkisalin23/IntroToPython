# Chapter 5 -  Dictionaries & Sets

# Dictionaries
    Dictionary = an unordered, mutable collection of items, where each item is stored as a key-value pair.

        # Basic Operations

            1. Creating a Dictionary

                # Creating a dictionary
                my_dict = {
                    'name': 'Salin',
                    'age': 25,
                    'city': 'Pittsburgh'
                }

            2. Accessing Values

                # Accessing values
                print(my_dict['name'])  # Output: Salin

            3. Adding or Updating Values

                # Adding a new key-value pair
                my_dict['email'] = 'Salin@example.com'

                # Updating an existing key-value pair
                my_dict['age'] = 26

# Properties of a Python Dictionaries

    1. It is unordered
    2. It is mutable - can be changed after it has been created
    3. It is indexed
    4. Cannot contain duplicate keys

# Methods of a Python Dictionaries

Python dictionaries come with a variety of built-in methods that make it easier to manage and manipulate them.

    ex: 

        - clear()
            Removes all items from the dictionary.
            my_dict.clear()

        - copy()
            Returns a shallow copy of the dictionary.
            new_dict = my_dict.copy()

        - fromkeys(iterable, value=None)
            Creates a new dictionary with keys from the given iterable and values set to the specified value.
            keys = ['a', 'b', 'c']
            new_dict = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}

        - get(key, default=None)
            Returns the value for the specified key if the key is in the dictionary, otherwise returns the default value.
            value = my_dict.get('key1', 'default_value')
        
        - items()
            Returns a view object that displays a list of a dictionary's key-value tuple pairs.
            items = my_dict.items()

        - keys()
            Returns a view object that displays a list of all the keys in the dictionary.
            keys = my_dict.keys()

        - pop(key, default=None)
            Removes the specified key and returns the corresponding value. If the key is not found, returns the default value.
            value = my_dict.pop('key1', 'default_value')

        - popitem()
            Removes and returns the last key-value pair added to the dictionary.
            key, value = my_dict.popitem()
        
        - setdefault(key, default=None)
            Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.
            value = my_dict.setdefault('key1', 'default_value')

        - update([other])
            Updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.
            my_dict.update({'key2': 'value2', 'key3': 'value3'})

        - values()
            Returns a view object that displays a list of all the values in the dictionary.
            values = my_dict.values()

# Example Usage:
    
        # Creating a dictionary
        my_dict = {'name': 'Salin', 'age': 23, 'city': 'Pittsburgh'}

        # Using the get method
        print(my_dict.get('name'))  # Output: Salin
        print(my_dict.get('email', 'Not Available'))  # Output: Not Available

        # Using the items method
        print(my_dict.items())  # Output: dict_items([('name', 'Salin'), ('age', 23), ('city', 'Pittsburgh')])

        # Using the keys method
        print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

        # Using the values method
        print(my_dict.values())  # Output: dict_values(['Salin', 23, 'Pittsburgh'])

        # Using the update method
        my_dict.update({'email': 'Salin@example.com'})
        print(my_dict)  # Output: {'name': 'Salin', 'age': 23, 'city': 'Pittsburgh', 'email': 'Salin@example.com'}

        # Using the pop method
        age = my_dict.pop('age')
        print(age)  # Output: 23
        print(my_dict)  # Output: {'name': 'Salin', 'city': 'Pittsburgh', 'email': 'Salin@example.com'}

        # Using the popitem method
        last_item = my_dict.popitem()
        print(last_item)  # Output: ('email', 'Salin@example.com')
        print(my_dict)  # Output: {'name': 'Salin', 'city': 'Pittsburgh'}

        # Using the setdefault method
        city = my_dict.setdefault('city', 'Los Angeles')
        print(city)  # Output: Pittsburgh
        print(my_dict)  # Output: {'name': 'Salin', 'city': 'Pittsburgh'}

        # Using the clear method
        my_dict.clear()
        print(my_dict)  # Output: {}

# Sets

Sets = an unordered collection of unique items. Sets are mutable, but they do not support duplicate elements.

    # Basic Operations

    1. Creating a Set
        # Creating a set
        my_set = {1, 2, 3, 4, 5}

    2. Adding Elements
        # Adding a single element
        my_set.add(6)

        # Adding multiple elements
        my_set.update([7, 8, 9])

    3. Removing Elements
        # Removing an element (will raise a KeyError if the element is not present)
        my_set.remove(3)

        # Removing an element (will not raise an error if the element is not present)
        my_set.discard(10)

        # Removing an element and returning it
        element = my_set.pop()

    4. Checking if an Element Exists
        # Checking if an element exists
        if 5 in my_set:
            print('5 is in the set')

# Set Operations
    - Union
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        union_set = set1 | set2  # or set1.union(set2)

    - Intersection
        intersection_set = set1 & set2  # or set1.intersection(set2)

    - Difference
        difference_set = set1 - set2  # or set1.difference(set2)

    - Symmetric Difference
        symmetric_difference_set = set1 ^ set2  # or set1.symmetric_difference(set2)

# Example Usage:

    # Example dictionary
    student_scores = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78
    }

    # Example set
    passed_students = {'Alice', 'Bob', 'Eve'}

    # Adding a new student score
    student_scores['David'] = 88

    # Checking who passed
    for student in student_scores:
        if student in passed_students:
            print(f"{student} passed with a score of {student_scores[student]}")