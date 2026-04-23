def total_average_price(*args) :
    total_price = 0 
    for price in args:
        total_price += price 
    average_price = total_price / len(args) 
    return total_price, average_price

total, average = total_average_price(13.0, 22.5, 21.50, 10.50)
print("Total Price:", total)    
print("Average Price:", average)