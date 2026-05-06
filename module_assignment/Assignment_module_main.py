import Assingment_module_math_util as math_utils

def main():

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    operation = input("Enter the operation (+, -, *, /): ")

    match operation:
        case "+":
            result = math_utils.add(num1, num2)
        case "-":
            result = math_utils.subtract(num1, num2)
        case "*":
            result = math_utils.multiply(num1, num2)
        case "/":
            result = math_utils.divide(num1, num2)

    print(f"The result is: {result}")

main()