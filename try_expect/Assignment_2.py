first_input = input("Enter the first number: ")
second_input = input("Enter the second number: ")

try:
    num1 = float(first_input)
    num2 = float(second_input)
    
    result = num1 / num2
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Cannot divide by zero. Please enter a valid second number.")
except:
    print("Invalid input. Please enter valid numbers.")