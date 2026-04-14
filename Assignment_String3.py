#write a program to count occurrences of all characters witnin a string?
txt = "hello world"
char_count = {} 
for char in txt:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
for char, count in char_count.items():
    print(char + ": " + str(count))