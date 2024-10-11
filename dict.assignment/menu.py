restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
print("Before update:", restaurant_menu)

# Add a new category called "Beverages" with at least two items.
restaurant_menu["Drinks"] = {"Coke products": 2.99, "Sweet tea": 2.99}

# Update the price of "Steak" to 17.99.
restaurant_menu["Main Course"]["Steak"] = 17.99

# Remove "Bruschetta" from "Starters".
restaurant_menu["Starters"].pop("Bruschetta")

print("After update:", restaurant_menu)