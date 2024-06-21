#Create a simple calculate 
num1 = input("Enter a number: ")
num1 = int(num1)

num2 = input("Enter a number: ")
num2 = int(num2)

operator = input("""
Enter 1 to add
Enter 2 to Subtract
Enter 3 to Multiply
Enter 4 to Divide: """)
operator = int(operator)

if(operator == 1):
    print(num1 + num2)
elif(operator == 2):
    print(num1 - num2)
elif(operator == 3):
    print(num1 * num2)
else:
    print(num1 / num2)