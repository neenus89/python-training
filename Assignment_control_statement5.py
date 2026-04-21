n = int(input("Enter the upper limit: "))

for num in range(2, n + 1):
    for i in range(2, int(num/2) + 1):
        if (num % i) == 0:
            break
    else:
        print(num)