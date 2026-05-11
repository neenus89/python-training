import datetime

age = input("Enter your age: ")
try:
    age = int(age)
    if(age < 0) :
        raise Exception()
    else:
        birth_year = datetime.datetime.now().year - age
        print(f"Year of birth {birth_year}")
except Exception:
    print("Age cannot be negative. Please enter a valid age.")


