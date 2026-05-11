import re

password = input("Enter a password: ")
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

check_valid = re.search(pattern, password)
if check_valid:
    print("Valid password.")
else:
    print("Invalid password")