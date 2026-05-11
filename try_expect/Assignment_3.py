def convert_string_to_first_letter_upper(input_string):
    try:
        if not input_string.isalpha():
            raise TypeError()
        result = input_string.capitalize()
        return result
    except TypeError:
        print("Input string contains numbers. Please enter a valid string.")
    except:
        print("An error occurred while processing the string.")

user_input = input("Enter a string: ")
converted_string = convert_string_to_first_letter_upper(user_input)

if converted_string:
    print("Converted string:", converted_string)
    
    
    