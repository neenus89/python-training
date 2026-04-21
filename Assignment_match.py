items = {
    "Chicken" : 120,
    "Beef" : 150,
    "Veg" : 100
}

item_name = input("Enter the item name: ")

match item_name.lower():
    case "chicken":
        print("The price of Chicken is", items["Chicken"])
    case "beef":
        print("The price of Beef is", items["Beef"])    
    case "veg":
        print("The price of Veg is", items["Veg"])
    case _:
        print("Item not found.")