a = 12
s = "Hello"

try:
    print(a + s)
except TypeError:
    print("Cannot add an integer and a string.")