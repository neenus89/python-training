
n = int(input("Enter a number   "))

user_input = input("Enter numbers separated by spaces upto n   ")

actual_set = set()
for x in user_input.split():
    actual_set.add(int(x))


expected_set = set()
i = 1

while i <= n:
    expected_set.add(i)
    i = i + 1

print("Expected numbers:", expected_set)  


#Subtract the sets to find the difference
missing_set = expected_set - actual_set

print("Missing numbers:", missing_set)