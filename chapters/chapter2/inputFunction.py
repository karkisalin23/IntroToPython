# Take input from the user without a prompt
user_input = input()
print("You entered:", user_input)

# Take input from the user with a prompt
user_name = input("Enter your name: ")
print("Hello,", user_name)

# Take numeric input from the user
age_str = input("Enter your age: ")
age = int(age_str)  # Convert the input string to an integer
print("Your age is:", age)

# Take multiple inputs in one line
input_str = input("Enter your first name and age separated by a space: ")
first_name, age_str = input_str.split()  # Split input string
age = int(age_str)  # Convert the age to an integer
print("Name:", first_name)
print("Age:", age)
