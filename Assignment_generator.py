#Define a generator that will extract vowels from a given string and print them one by one

def vowel_generator(input_string):
    for char in input_string:
        if char.lower() in 'aeiou':
            yield char

input_string = input("Enter a string: ")
for vowel in vowel_generator(input_string):
    print(vowel)