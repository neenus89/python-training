#Write a program to find words with both alphabets and numbers from an input string?
print('Enter a string:')
txt = input()
words = txt.split()
result = []
for word in words:
    if any(char.isalpha() for char in word):
        result.append(word)
    if any(char.isdigit() for char in word):
        result.append(word)
print(result)