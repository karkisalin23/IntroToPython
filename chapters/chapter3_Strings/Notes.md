# Chapter 3 - Strings

# String:
    String - a sequence of characters enclosed within either single quotes (' '), double quotes (" "), or triple quotes (''' ''', """ """).Strings are immutable, meaning once they are created, their contents cannot be changed.

        ex: 
            single quotes --> a = 'Hello'
            double quotes --> b = "Hello"
            triple quotes --> c = '''Hello''' or """Hello"""

# String Slicing:
    String Slicing - process of extracting a portion of a string by specifying a range of indices.

        ex:
            name = "H e l l o"  --> length 5
                    0 1 2 3 4

        The index in a string start from 0 to (length - 1) in Python. In order to slice a string, we use the following syntax:

            sl = name[index_start : index_end]

                s = "Hello, World!"

                # Get the substring "Hello"
                print(s[0:5])

                # Get the substring "World!"
                print(s[7:])

                # Get the substring "World"
                print(s[7:12])

                # Get every second character
                print(s[::2])

                # Reverse the string
                print(s[::-1])

# Escape Sequences:
    Escape sequences - used to insert characters that are not easy to include directly in a string. They start with a backslash ('\').
        ex:
        
            # Newline character
            print("Hello,\nWorld!")  # Output: Hello,
                                     #         World!

            # Tab character
            print("Hello,\tWorld!")  # Output: Hello,    World!

            # Backslash character
            print("This is a backslash: \\")  # Output: This is a backslash: \

            # Single quote character
            print('It\'s a wonderful day!')  # Output: It's a wonderful day!

            # Double quote character
            print("She said, \"Hello!\"")  # Output: She said, "Hello!"

            # Carriage return
            print("Hello,\rWorld!")  # Output: World!

            # Backspace
            print("Hello, \bWorld!")  # Output: Hello,World!

            # Formfeed
            print("Hello,\fWorld!")  # Output: Hello,
                                     #         World!

            # Unicode character (e.g., smiley face)
            print("Here is a smiley face: \u263A")  # Output: Here is a smiley face: ☺

            # Octal value (e.g., newline)
            print("Hello,\012World!")  # Output: Hello,
                                       #         World!

            # Hexadecimal value (e.g., newline)
            print("Hello,\x0AWorld!")  # Output: Hello,
                                       #         World!
