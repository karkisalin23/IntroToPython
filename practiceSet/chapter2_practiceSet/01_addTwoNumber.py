#1) Write a Python program to add two numbers
userInput = input("Enter 2 number to add seperated by space: ")
num1, num2 = userInput.split() # Split input string
int_num1 = int(num1) # Convert to an integer
int_num2 = int(num2) # Convert to an integer

result = int_num1 + int_num2
print(f"The sum of {int_num1} and {int_num2} is",result)

