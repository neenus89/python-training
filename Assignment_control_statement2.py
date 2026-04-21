n = 50
sum = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    sum += i
print("The sum of odd numbers from 1 to", n, "is:", sum)