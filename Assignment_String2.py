#Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first?
txt = "HeLlO WoRLd"
lowercase_letters = ""  
uppercase_letters = ""
for char in txt:
    if char.islower():
        lowercase_letters += char
    elif char.isupper():
        uppercase_letters += char
result = lowercase_letters + uppercase_letters
print(result)