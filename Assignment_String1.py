#.Write a program to create a new string made of an input string’s first, middle, and last character.?
print('Enter your a string:')
txt = input()
first_char = txt[0]
middle_char = txt[len(txt)//2]
last_char = txt[-1]
new_string = first_char + middle_char + last_char
print(new_string)