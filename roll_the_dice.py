import random

def roll_dice():
    return random.randint(1, 6)

def roll_the_dice_game():
    user_total = 0
    computer_total = 0

    while True:
        user_choice = input("Press 'r' to roll the dice or 's' to stop: ").lower()

        if user_choice == 'r':
            user_roll = roll_dice()
            computer_roll = roll_dice()

            print(f"\nYou rolled: {user_roll}")
            print(f"Computer rolled: {computer_roll}")

            user_total += user_roll
            computer_total += computer_roll
        elif user_choice == 's':
            break
        else:
            print("Invalid input. Please try again.")

    print(f"\nYour total: {user_total}")
    print(f"Computer total: {computer_total}")

    if user_total > computer_total:
        print(f"\nCongratulations! You won with a total of {user_total}.")
    elif user_total < computer_total:
        print(f"\nSorry, the computer won with a total of {computer_total}.")
    else:
        print("\nIt's a tie!")

roll_the_dice_game()