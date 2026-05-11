import re

sentance = input("Enter a sentence: ")
numbers = re.findall(r'\d+', sentance)
print("Numbers found:", numbers)