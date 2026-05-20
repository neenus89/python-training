def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

gen = even_numbers()

print(next(gen))
print(next(gen))
print(next(gen))