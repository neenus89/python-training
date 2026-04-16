my_list = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [x for x in my_list if x % 2 == 0]
print(even_numbers)
print("count of even numbers in the list is: ", len(even_numbers))

odd_numbers = [x for x in my_list if x % 2 != 0]
print(odd_numbers)
print("count of odd numbers in the list is: ", len(odd_numbers))