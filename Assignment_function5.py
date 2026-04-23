def check_zero(func):
    def innerfun(a, b):
        if b == 0:
            return "Cannot be divided by zero"
        
        return func(a, b)
    
    return innerfun

@check_zero
def devide(a, b) :
    return a / b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


result = devide(a, b)
print(result)