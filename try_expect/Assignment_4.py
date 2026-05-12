import datetime

class NegativeAgeException(Exception):
    pass

age = input("Enter your age: ")
try:
    age = int(age)
    if(age < 0) :
        raise NegativeAgeException()
    else:
        birth_year = datetime.datetime.now().year - age
        print(f"Year of birth {birth_year}")
except NegativeAgeException:
    print("Age cannot be negative. Please enter a valid age.")


