n = int(input("Enter a number: "))

limit = 10

print("----- Multiplication Table of", n, "-----")
for i in range(1, limit + 1):
   print(f"{i}*{n}={i*n}")