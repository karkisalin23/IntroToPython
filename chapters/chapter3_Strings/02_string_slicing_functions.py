# Assign the string "Hello, World!" to the variable 'greeting'
greeting = "Hello, World!"

# Print the type of the variable 'greeting', which is a string
print(type(greeting))  # Output: <class 'str'>

# Print the value of the variable 'greeting'
print(greeting)  # Output: Hello, World!

# Print the first character of 'greeting'
print(greeting[0])  # Output: H

# Get and print the substring "Hello" from 'greeting'
print(greeting[0:5])  # Output: Hello

# Get and print the substring "World!" from 'greeting'
print(greeting[7:])  # Output: World!

# Get and print the substring "World" from 'greeting'
print(greeting[7:12])  # Output: World

# Get and print every second character from 'greeting'
print(greeting[::2])  # Output: Hlo ol!

# Reverse the string 'greeting' and print it
print(greeting[::-1])  # Output: !dlroW ,olleH

"""
String Functions
"""

# Print the length of the string 'greeting'
print(len(greeting))  # Output: 13

# Check if the string stored in 'greeting' ends with "rld" and print the result
print(greeting.endswith("rld"))  # Output: True if 'greeting' ends with "rld", otherwise False

# Count the occurrences of the character "e" in 'greeting' and print the result
print(greeting.count("e"))  # Output: Number of times "e" appears in 'greeting'

# Capitalize the first character of string and make all other characters lowercase, then print the result
print(greeting.capitalize())  # Output: 'Hello, world!' if 'hello, World!' was not already capitalized and in lowercase

# Find the first occurrence of the substring "World!" in 'greeting' and print the result
# This will return the index of the first character of the first match of "World!" in 'greeting', or -1 if not found
print(greeting.find("World!"))  # Output: Starting index of "World!" in 'greeting', or -1 if not found

# Replace the substring "World!" with "Everyone!" in 'greeting' and print the result
print(greeting.replace("World!", "Everyone!"))  # Output: A new string where "World!" is replaced with "Everyone!" in 'greeting'

