#Ask user for their name
name = input("What's your name? ")

#Ask user for their age
age = input("How old are you? ")

#return/output the user input
# print("Hello " + name + ", you are " + age + " years old.")

print(f"Hello {name}, you are {age} years old.")
print()
print("Hello {}, you are {} years old.".format(name, age))
