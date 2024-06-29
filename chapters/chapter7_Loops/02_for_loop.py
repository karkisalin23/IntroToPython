# List of anime
animes = ["Naruto", "Attack on Titan", "Jujutsu Kaisen", "Classroom of the Elite", 
          "Bleach", "Black Clover", "Dororo", 86]

# Iterating over the list of anime and printing each anime
for anime in animes:
    print(anime)

#for loop with an else block
for i in range(10):
    print(i)
else:
    # This block executes when the for loop completes normally (i.e., no break)
    print("This is inside else of for loop")

# break statement
"""
The 'break' statement in Python is used to terminate the nearest enclosing loop.
It allows you to exit a loop prematurely based on a specific condition, bypassing
the normal termination condition of the loop.
"""

# 'break' in loop
for i in range(10):
    print(i)
    if i == 5:
        # Terminating the loop when i equals 5
        break
else:
    # This block will not execute because the loop is terminated by break
    print("This is inside else of for loop")

# Continue statement
for i in range(10):
    if i == 5:
        # Skip the rest of the loop body and continue with the next iteration
        continue
    print(i)
else:
    # This block executes when the for loop completes normally (i.e., no break)
    print("This is inside else of for loop")

# The pass statement
i = 4

# Conditional check
if i > 0:
    # The pass statement is a placeholder that does nothing
    pass

# Print statement to demonstrate that the code continues execution
print("Pass Statement is 'null' in python")
