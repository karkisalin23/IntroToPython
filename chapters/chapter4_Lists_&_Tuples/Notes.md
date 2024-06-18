# Chapter 4

In Python, lists and tuples are both used to store collections of items, but they have some key differences in terms of mutability, syntax, and intended use cases. Here's a breakdown of each:

# Lists:

    - Mutable: Lists are mutable, meaning their elements can be changed after the list is created.
    - Syntax: Defined using square brackets [].
    - Usage: Ideal for sequences of items where the order and number of elements might change.

        ex:
            
            my_list = [1, 2, 3, 4, 5]

# List Methods: 
Python lists come with a variety of methods that allow you to perform different operations on them. Here are some commonly used list methods:

    ex:
        1. append(item)
            - Adds an item to the end of the list.

                my_list = [1, 2, 3]
                my_list.append(4)
                # my_list is now [1, 2, 3, 4]

        2. extend(iterable)
            -Extends the list by appending elements from the iterable.

                my_list = [1, 2, 3]
                my_list.extend([4, 5, 6])
                # my_list is now [1, 2, 3, 4, 5, 6]

        3. insert(index, item)
            - Inserts an item at a given position.

                my_list = [1, 2, 4]
                my_list.insert(2, 3)
                # my_list is now [1, 2, 3, 4]

        4. remove(item)
            -Removes the first occurrence of an item.

                my_list = [1, 2, 3, 2, 4]
                my_list.remove(2)
                # my_list is now [1, 3, 2, 4]

        5. pop([index])
            - Removes and returns the item at the given position (default is the last item).

                my_list = [1, 2, 3]
                item = my_list.pop()
                # item is 3, my_list is now [1, 2]

        6. clear()
            -Removes all items from the list.

                my_list = [1, 2, 3]
                my_list.clear()
                # my_list is now []
        
        7. index(item, [start, [end]])
            - Returns the index of the first occurrence of an item.

                my_list = [1, 2, 3, 2, 4]
                index = my_list.index(2)
                # index is 1
                
        8. count(item)
            - Returns the number of occurrences of an item.

                my_list = [1, 2, 2, 3, 2, 4]
                count = my_list.count(2)
                # count is 3

        9. sort(key=None, reverse=False)
            - Sorts the list in ascending order (can be customized with key and reverse).

                my_list = [3, 1, 4, 2]
                my_list.sort()
                # my_list is now [1, 2, 3, 4]

        10. reverse()
            - Reverses the elements of the list in place.

                my_list = [1, 2, 3, 4]
                my_list.reverse()
                # my_list is now [4, 3, 2, 1]

        11. copy()
            - Returns a shallow copy of the list.

                my_list = [1, 2, 3]
                new_list = my_list.copy()
                # new_list is [1, 2, 3]


# Example Code Using Various Methods: 

            # Creating a list
            fruits = ['apple', 'banana', 'cherry']

            # Append an item
            fruits.append('date')
            print(fruits)  # ['apple', 'banana', 'cherry', 'date']

            # Extend the list
            fruits.extend(['elderberry', 'fig'])
            print(fruits)  # ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

            # Insert an item at a specific position
            fruits.insert(1, 'blueberry')
            print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry', 'fig']

            # Remove an item
            fruits.remove('banana')
            print(fruits)  # ['apple', 'blueberry', 'cherry', 'date', 'elderberry', 'fig']

            # Pop an item
            last_fruit = fruits.pop()
            print(last_fruit)  # 'fig'
            print(fruits)  # ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

            # Clear the list
            fruits.clear()
            print(fruits)  # []

            # Re-create the list
            fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

            # Find the index of an item
            index = fruits.index('cherry')
            print(index)  # 2

            # Count occurrences of an item
            count = fruits.count('apple')
            print(count)  # 1

            # Sort the list
            fruits.sort()
            print(fruits)  # ['apple', 'banana', 'cherry', 'date', 'elderberry']

            # Reverse the list
            fruits.reverse()
            print(fruits)  # ['elderberry', 'date', 'cherry', 'banana', 'apple']

            # Copy the list
            new_fruits = fruits.copy()
            print(new_fruits)  # ['elderberry', 'date', 'cherry', 'banana', 'apple']

These methods provide a wide range of functionality to manipulate and interact with lists effectively in Python.

# Tuples:

    - Immutable: Tuples are immutable, meaning once they are created, their elements cannot be changed.
    - Syntax: Defined using parentheses (), although they can also be defined without parentheses.
    - Usage: Used for fixed collections of elements that are not intended to be changed, such as coordinates, database records, etc.

    ex:

        my_tuple = (1, 2, 3, 4, 5)
        # or without parentheses
        my_tuple = 1, 2, 3, 4, 5

# Tuples Methods

In Python, tuples are immutable sequences typically used to store collections of heterogeneous data. They support various methods and operations that allow you to work with the data they contain. Here are the primary methods and operations you can use with tuples:

    # Methods

        Since tuples are immutable, they have very few methods:

            1. count()
                Returns the number of times a specified value appears in the tuple.
                t = (1, 2, 3, 2, 4)
                print(t.count(2))  # Output: 2

            2. index()
                Returns the index of the first occurrence of a specified value in the tuple.
                t = (1, 2, 3, 2, 4)
                print(t.index(2))  # Output: 1

    # Operations
        Tuples support various operations similar to lists, including indexing, slicing, and concatenation. Here are some common operations:

            1. Indexing
                Access an element by its index.
                t = (1, 2, 3)
                print(t[0])  # Output: 1

            2. Slicing
                Access a range of elements.
                t = (1, 2, 3, 4, 5)
                print(t[1:3])  # Output: (2, 3)

            3. Concatenation
                Combine tuples using the + operator.
                t1 = (1, 2)
                t2 = (3, 4)
                t3 = t1 + t2
                print(t3)  # Output: (1, 2, 3, 4)

            4. Repetition
                Repeat the elements of a tuple using the * operator.
                t = (1, 2)
                print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)

            5. Membership
                Check if an element exists in the tuple using the in keyword.
                t = (1, 2, 3)
                print(2 in t)  # Output: True
                print(4 in t)  # Output: False

            6. Length
                Get the number of elements in the tuple using the len() function.
                t = (1, 2, 3)
                print(len(t))  # Output: 3

            7. Iteration
                Iterate over the elements in a tuple using a for loop.
                t = (1, 2, 3)
                for item in t:
                    print(item)
                # Output:
                # 1
                # 2
                # 3

            8. Unpacking
                Assign the elements of a tuple to multiple variables.
                t = (1, 2, 3)
                a, b, c = t
                print(a, b, c)  # Output: 1 2 3
                
These methods and operations provide a robust way to work with tuples in Python, despite their immutability.

# Key Differences:

    - Mutability: Lists are mutable (can be changed), tuples are immutable (cannot be changed).
    - Performance: Tuples are generally faster than lists when it comes to iteration and indexing, partly because of their immutability.
    - Syntax: Lists are defined using [], while tuples can be defined with or without ().

# When to Use Which?

    - Use lists when you have a collection of items that may need to be modified, such as adding or removing elements.
    - Use tuples when you have a collection of items that should not change, such as coordinates of a point, database records fetched from a query, etc. 
    - They are also useful for returning multiple values from a function.

        ex:

            # List example
            shopping_list = ['apples', 'bananas', 'oranges']

            # Tuple example
            coordinates = (10, 20)

In summary, lists and tuples are both used for storing collections of items, but their mutability and intended use cases differentiate them. Lists are mutable and more flexible, while tuples are immutable and faster for certain operations.
