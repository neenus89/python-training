
actual_set = {1, 2, 4, 6, 8, 10}
n = 10

expected_set = set()
i = 1

while i <= n:
    expected_set.add(i)
    i = i + 1

print("Expected numbers:", expected_set)
print("Actual numbers:", actual_set)    


#Subtract the sets to find the difference
missing_set = expected_set - actual_set

print("Missing numbers:", missing_set)