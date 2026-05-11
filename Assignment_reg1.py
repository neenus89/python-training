import re

email = input("Enter an email address: ")
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

check_valid = re.search(pattern, email)
if check_valid:
    print("Valid email address.")   
else:
    print("Invalid email address.")