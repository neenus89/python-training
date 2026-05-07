#Accept employees Sign In and Sign out time and calculate number of hour worked
 
from datetime import datetime

sign_in_input = input("Enter Sign In time (HH:MM): ")
sign_out_input = input("Enter Sign Out time (HH:MM): ")

sign_in_time = datetime.strptime(sign_in_input, "%H:%M")
sign_out_time = datetime.strptime(sign_out_input, "%H:%M")

time_worked = sign_out_time - sign_in_time

hours_worked = time_worked.total_seconds() / 3600

print(f"The number of hours worked = {hours_worked:.2f}")