"""
Write a program to fill in a letter template given below with name and date.
    letter = Dear <|name|>,
             You are selected!
             <|Date|>
"""

#User input
name = input("Enter your name: ")
date = input("Enter a date: ")

#letter
letter = '''
    Dear <|name|>,

I hope this letter finds you in good health and spirits. I am writing to remind you about our upcoming meeting.

Please be present on <|date|>.

Looking forward to seeing you.

Best regards,
[Your Name]
"""
        '''

#replace <|name|> and <|date|> from letter to user input name and date
letter = letter.replace("<|name|>", name)
letter = letter.replace("<|date|>", date)

#print the letter with user input name and date
print(letter)