letter = '''Dear <|NAME|>,
You are selected!


  
Date:<|DATE|>
'''
name = input("Enter your name\n")
name = input("Enter Date\n")
print(letter)
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",name)
print(letter)