products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]
#print(products)

# Create and print a dictionary
#for x in products:
#    print(x)

# Get the value of the "name" key:
#x = products[1]["name"]
#print("Product 1 name is " + str(x))

# Get the value of the "name" key using get:
#x = products[1].get("name")
#print("Using get method product 1 name is " + str(x))

# Change the "price" of product[1] to $1 higher:
#products[1]["price"] += 1
#print("Price of product 1 changed to " + str(products[1]["price"]))
#
# Print all key names in the product[1], one by one:
#rint("These are the keys of products[1]")
#or x in products[1]:
# print(x)
#
# Print all values in the product[1], one by one:
#rint("These are the values of products[1]")
#or x in products[1]:
# print(products[1][x])
#
# Doing the same using .values accessor:
#rint("These are the values using .values accessor")
#or x in products[1].values():
# print(x)
#
# Loop through both keys and values, by using the items() function:
#print("****************************************")

print("-----------------------")
print("THERE ARE 20 PRODUCTS")
print("-----------------------")
for x in products:
    print("Details of product " + str(x["id"])+ " : ")
    print("-------------------------")
    print("+ " +str(x["name"])+ " ($" +str(x["price"])+ ")")
    for y, z in x.items():
        print("The " +str(y)+ " is " + str(z))
    print("****************************************")

