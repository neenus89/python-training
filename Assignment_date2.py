#Accept two dates and find number of days between these two dates.

from datetime import datetime

date1_input = input("Enter the first date (YYYY-MM-DD): ")
date2_input = input("Enter the second date (YYYY-MM-DD): ")

date1 = datetime.strptime(date1_input, "%Y-%m-%d")
date2 = datetime.strptime(date2_input, "%Y-%m-%d")  

difference = date2 - date1

print(f"The number of days = {difference.days}")

