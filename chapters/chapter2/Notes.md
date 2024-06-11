# Chapter 2 Notes

1) Variable:
    Variable = name given to a memory location which are used to store values

        ex:
            a = 10 -- Store 10 in memory
            name = "Salin" --Store Salin in memory

        Rules for defining a variable name --> also applies to other identifiers
            - A variable name can contain alphablets, digits, and underscore
            - A variable name can only start with an alphablets
            - A variable name cannot start with a digit
            - No whitespace is allowed to be used inside a variable name.# Taking multiple inputs in one line

2) Datatype:
    Datatype = an attribute associated with a piece of data that tells a computer how to interpret its value

        ex:
            Integers - number without decimal
            Floating point numbers - numbers that have a decimal point
            String - a sequence of characters used to represent text
            Boolean - a data type that has one of two possible values: True or False
            None - used to represent the absence of a value or a null value

3) Operators:
    Operators - symbols or keywords that represents a specific mathematical or logical action or process

        Following are some common operators in Pythons
            - Arithmetic operators  =    +, -, *, /, %, etc...
            - Assignment Operators  =    =, +=, -=, etc...
            - Comparison Operators  =    ==, <, >, <=, =>, !=, etc... - return boolean
            - Logical Operators     =    and, or, not - operate in Boolean

4) type() function and Typecasting:
    In Python, the 'type()' function and typecasting (or type conversion) are two essential concepts related to data types. Here's an explanation of both:

        type() function - used to determine the type of an object. It returns the type of the object passed as an argument.

            Syntax:
                type(object)

            # Checking the type of different objects
                print(type(5))                    # Output: <class 'int'>
                print(type(3.14))                 # Output: <class 'float'>
                print(type("Hello"))              # Output: <class 'str'>
                print(type([1, 2, 3]))            # Output: <class 'list'>
                print(type((1, 2, 3)))            # Output: <class 'tuple'>
                print(type({1, 2, 3}))            # Output: <class 'set'>
                print(type({'a': 1, 'b': 2}))     # Output: <class 'dict'>


        Typecasting (Type Conversion) - the process of converting a value from one type to another.

            Common Typecasting Functions
                - int(x) - Converts x to an integer.
                - float(x) - Converts x to a floating-point number.
                - str(x) - Converts x to a string.
                - list(x) - Converts x to a list.
                - tuple(x) - Converts x to a tuple.
                - set(x) - Converts x to a set.
                - dict(x) - Converts x to a dictionary (from a sequence of key-value pairs).

            ex:
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

5) input() Function:
    input() - is used to take input from the user. It reads a line from the input and returns it as a string.
    
        ex:
            # Taking input from the user without a prompt
                user_input = input()
                print("You entered:", user_input)

            # Taking input from the user with a prompt
                user_name = input("Enter your name: ")
                print("Hello,", user_name)

            # Taking numeric input from the user
                age_str = input("Enter your age: ")
                age = int(age_str)  # Converting the input string to an integer
                print("Your age is:", age)
                print("In 5 years, you will be:", age + 5)

            # Taking multiple inputs in one line
                input_str = input("Enter your first name and age separated by a space: ")
                first_name, age_str = input_str.split()  # Splitting the input string
                age = int(age_str)  # Converting the age to an integer
                print("Name:", first_name)
                print("Age:", age)
