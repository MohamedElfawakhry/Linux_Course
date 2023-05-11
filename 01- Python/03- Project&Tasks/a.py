# Define the grocery items and their prices as tuples
grocery_items = (
    ("apple", 1.0),
    ("banana", 0.5),
    ("bread", 2.0),
    ("milk", 1.5),
)

# Ask the user for the quantity of each item they want to buy
quantities = []
for item in grocery_items:
    quantity = int(input(f"How many {item[0]}s do you want to buy? "))
    quantities.append(quantity)

# Calculate the total cost of the items
total_cost = 0.0
for i in range(len(grocery_items)):
    item_cost = grocery_items[i][1] * quantities[i]
    total_cost += item_cost

# Print the receipt with the item names, quantities, and costs
print("Receipt")
print("--------")
for i in range(len(grocery_items)):
    item_cost = grocery_items[i][1] * quantities[i]
    print(f"{grocery_items[i][0]} x {quantities[i]} = {item_cost}")
print(f"Total cost: {total_cost}")