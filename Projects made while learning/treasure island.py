choice1 = input("Welcome to Treasure Island. \nPrint you are at a cross road.Where do you want to go? 'left' or 'right \n")
if choice1 == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input("type 'wait' to wait for a boat or 'swim' to swim across \n")
    if choice2 == 'wait':
        print("You arrive at an island unharmed.")
        choice3 = input("There are 3 doors to enter type 'red' to enter the red door 'blue' to enter the blue door 'yellow' to enter the Yellow door\n" )
        if choice3 == 'red':
            print("You were burned.Try again!")
        elif choice3 == 'blue':
            print("You were Eaten by beasts.Try again!")
        elif choice3 == 'yellow':
            print("You Win!")
        else:
            print("Invalid")
            exit()
    else:
        ("You were attacked by trouts.Try again!")
else:
    print("You fell in a hole.Try again!")

