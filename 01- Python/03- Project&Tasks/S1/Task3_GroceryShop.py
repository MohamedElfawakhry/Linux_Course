
AvailableItems = (
    ("apple", 1.0),
    ("banana", 0.5),
    ("bread", 2.0),
    ("milk", 1.5),
    ("Coffe",2.5),
)

UserName = input("Please Enter Your Name : ")
WelcomeMSG = "Welcome {} to Our shop".format(UserName)
lenWCMSG = len(WelcomeMSG)
print("*"*lenWCMSG)
print(WelcomeMSG)
print("*"*lenWCMSG)

# Ask the user for the quantity of each item they want to buy
quantities = []
for item in AvailableItems :
    quantity = int(input(f"How Many {item[0]}s do you want ? "))
    quantities.append(quantity)

# Calculating the Receipt
total_cost  = 0.0
for i in range(len(AvailableItems)):
    item_cost = AvailableItems[i][1] * quantities[i]
    total_cost += item_cost 

# Print the receipt with the item names, quantities, and costs
print("---- Reciept ----")
for i in range(len(AvailableItems)):
    item_cost = AvailableItems[i][1] * quantities[i]
    print(f"{AvailableItems[i][0]} x {quantities[i]} = {item_cost}")
print(f"Total Cost = {total_cost}")



