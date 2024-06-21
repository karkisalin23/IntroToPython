# Chapter 6 - Condition Expressions

# Condition Expressions
    Conditional expressions = also known as ternary operators, allow you to evaluate conditions in a compact and readable way. 
    
    The basic syntax for a conditional expression is:

        value_if_true if condition else value_if_false
        
        if(condition):
            print(True)
        else:
            print(False)
    
    This can be broken down into three parts:
        - value_if_true: The value that will be assigned if the condition evaluates to True.
        - condition: The condition to evaluate.
        - value_if_false: The value that will be assigned if the condition evaluates to False.

    ex: 
        age = 23
        status = "Adult" if age >= 18 else "Minor"
        print(status)  # Output: Adult

# Logical Operators
    Logical Operators = logical operators are used to combine conditional statements.

        'and' Operator:
            The 'and' operator returns True if both operands are true.
            Ex:
                a = True
                b = False
                result = a and b  # result is False

        'or' Operator:
            The 'or' operator returns True if at least one of the operands is true.
            Ex:
                a = True
                b = False
                result = a or b  # result is True

        'not' Operator:
            The 'not' operator negates the boolean value of the operand.
            Ex:
            a = True
    
    # Detailed Examples:

        Using 'and'
            x = 5
            y = 10
            if x > 0 and y > 0:
                print("Both numbers are positive.")
            # Output: Both numbers are positive.

        Using 'or'
            x = 5
            y = -10
            if x > 0 or y > 0:
                print("At least one number is positive.")
            # Output: At least one number is positive.

        Using 'not'
            x = 5
            if not x < 0:
                print("x is not negative.")
            # Output: x is not negative.

    # Combining Logical Operators

        You can combine multiple logical operators to form complex conditions.

            x = 5
            y = 10
            z = 15

            if (x < y and y < z) or not (x
            == z):
                print("Complex condition is True.")
            # Output: Complex condition is True.
