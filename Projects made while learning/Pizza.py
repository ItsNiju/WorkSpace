size = input("Enter the desiered size S - Small , M - Medium , L - Large : ")
price = 0

if size == "S": 
    print("You have choosen a small sized pizza")
    price = 15
    add_pepperoni = input("Do you want to add pepperoni? Y or N : ")
    if add_pepperoni == "Y":
        price += 2
elif size == "M":
    print("You have choosen a medium sized pizza")
    price = 20 
    add_pepperoni = input("Do you want to add pepperoni? Y or N : ")
    if add_pepperoni == "Y":
        price += 3
elif size == "L":
    print("You have choosen a large sized pizza")
    price = 25
    add_pepperoni = input("Do you want to add pepperoni? Y or N : ")
    if add_pepperoni == "Y":
        price += 3
else:
    print("Invalid!")
    exit()
extra_cheese = input("Do you want extra Cheese? Y or N : ")
if extra_cheese == "Y":
    price += 1
print(f"You have chosen Size {size} pizza and it will cost you {price}$")

