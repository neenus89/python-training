#Define a generator that will print all the words of a sentence one by one.

def word_generator(sentence):
    for word in sentence.split():
        yield word

input_sentence = input("Enter a sentence: ")
for word in word_generator(input_sentence):
    print(word)