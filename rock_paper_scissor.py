import random

def rock_paper_scissors_game():
    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = random.choice(choices)

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == 'rock' and computer_choice == 'scissors' or \
             user_choice == 'paper' and computer_choice == 'rock' or \
             user_choice == 'scissors' and computer_choice == 'paper':
            print("Congratulations! You win!")
        else:
            print("Sorry, the computer wins.")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
            
rock_paper_scissors_game()