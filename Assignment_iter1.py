class VowelIterator:
    def __iter__(self, input_string=None):
        if input_string is not None:
            self.input_string = input_string
            self.index = 0
        return self

    def __next__(self):
        while self.index < len(self.input_string):
            char = self.input_string[self.index]
            self.index += 1
            if char.lower() in 'aeiou':
                return char
        raise StopIteration

my_string = "abcdefghijklmnopqrstuvwxyz" 

vowel_iterator = VowelIterator()

vowel_iterator.__iter__(my_string)

for vowel in vowel_iterator:
    print(vowel)