import random

user_choice = int(input("Enter 0 for rock, 1 for paper and 2 for scissors : "))
random_int = random.randint(0,2)


if user_choice < 3:
    print(f"The computer chose {random_int}")
    if user_choice == 0 and random_int == 2:
        print("You win!")
    elif random_int == 0 and user_choice == 2:
        print("You lose")
    elif random_int > user_choice:
        print("You lose")
    elif user_choice > random_int:
        print("You Win!")
    elif user_choice == random_int:
        print("Draw!")
    else:
        print("invalid")
else:
    print("Invalid")

