input_string = "Python is easy and Python is Powerful"
string_set = set(input_string.split())

unique_words = set()

for word in string_set:
    unique_words.add(word)

print("Unique words:", unique_words)