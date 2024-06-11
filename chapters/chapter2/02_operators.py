a = 1
b = 2

# Arithmetic operators
print("Arithmetic operators")
print(f"The value of {a} + {b} is ", a + b)
print(f"The value of {a} - {b} is ", a - b)
print(f"The value of {a} * {b} is ", a * b)
print(f"The value of {a} / {b} is ", a / b, "\n")

# Assignment Operators
print("Assignment Operators")
a = 34 # -- a is assign to be 34
a += 5 # -- assign vale of a + 5
print(a)

a = 34
a -= 5# assign vale of a - 5
print(a)

a = 34
a *= 5# assign vale of a * 5
print(a)

a = 34
a /= 5# assign vale of a / 5
print(a, "\n")

# Comparison Operators - return Boolean
print("Comparison Operators")
b = 5 > 7 # -- output will be false because 5 is not greater than 7
print(b)

b = 5 < 7 # -- output will be true because 7 is  greater than 5
print(b,"\n")

# Logical Operators - operate in Boolean
print("Logical Operators")
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is",(bool1 and bool2)) # and return True when both condition is match
print("The value of bool1 or bool2 is",(bool1 or bool2)) # or return True when one of the condition is true
print("The value of not bool2 is",(not bool2)) # return opposite of the condition