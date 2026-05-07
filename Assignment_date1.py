#Takes the user's date of birth as input  and calculate age in years
import datetime

birth_input = input("Enter your date of birth (YYYY-MM-DD): ")

birth_date = datetime.datetime.strptime(birth_input, "%Y-%m-%d")

birth_year = int(birth_date.strftime("%Y"))

today = datetime.date.today()

age = today.year - birth_year

print(f"You are {age} years old.")