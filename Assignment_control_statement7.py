items = {
    "Chicken" : 120,
    "Beef" : 150,
    "Veg" : 100
}

item_name = input("Enter the item name: ")

for item, price in items.items():
    if item.lower() == item_name.lower():
        print("The price of", item_name, "is", price)
        break
else:
    print("Item not found.")