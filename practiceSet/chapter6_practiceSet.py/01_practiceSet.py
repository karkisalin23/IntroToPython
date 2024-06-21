"""
Write a program to find greatest of 4 numbers enter by the user
"""
# Prompt the user to enter four numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

# Compare the first and fourth numbers to find the larger one and assign it to f1
if num1 > num4:
    f1 = num1
else:
    f1 = num4

# Compare the second and third numbers to find the larger one and assign it to f2
if num2 > num3:
    f2 = num2
else:
    f2 = num3

# Compare f1 and f2 to determine which is the largest number overall and print it
if f1 > f2:
    print(f"{str(f1)} is the greatest")
else:
    print(f"{str(f2)} is the greatest")

