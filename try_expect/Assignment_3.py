def convert_string_to_first_letter_upper(input_string):
        if not input_string.isalpha():
            raise TypeError()
        result = input_string.capitalize()
        return result

user_input = input("Enter a string: ")

try:
    converted_string = convert_string_to_first_letter_upper(user_input)
    print("Converted string:", converted_string)
except TypeError:
    print("Input string contains numbers. Please enter a valid string.")
except:
    print("An error occurred while processing the string.")

    
    
    
    