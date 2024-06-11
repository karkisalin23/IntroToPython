# Chapter 3 Notes

1) String:
    String - a sequence of characters enclosed within either single quotes (' '), double quotes (" "), or triple quotes (''' ''', """ """).Strings are immutable, meaning once they are created, their contents cannot be changed.

        ex: 
            single quotes --> a = 'Hello'
            double quotes --> b = "Hello"
            triple quotes --> c = '''Hello''' or """Hello"""

2) String Slicing:
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




