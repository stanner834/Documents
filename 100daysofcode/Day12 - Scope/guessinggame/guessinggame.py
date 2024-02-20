
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def display_logo():
    logo = """
  _____                               _____ _            _   _                 _               
 / ____|                             / ____| |          | \ | |               | |              
| |  __  ___ _ __ ___   ___  _ __   | |    | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
| | |_ |/ _ \ '_ ` _ \ / _ \| '_ \  | |    | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
| |__| |  __/ | | | | | (_) | | | | | |____| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
 \_____|\___|_| |_| |_|\___/|_| |_|  \_____|_| |_|\___| |_| \_|\__, |_| |_| |_|_.__/ \___|_|   
                                                                 __/ |                         
                                                                |___/                          
"""
    print(logo)

def play_game(difficulty):
    print("\nWelcome to the Number Guessing Game!")
    display_logo()

    # Initialize variables
    answer = random.randint(1, 100)
    turns = 10 if difficulty == "easy" else 5

    while turns > 0:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        guess = int(input("Guess a number between 1 and 100: "))

        if guess == answer:
            print("Congratulations! You guessed the correct number.")
            print(f"The answer was {answer}.")
            break
        elif guess < answer:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

        turns -= 1

    if turns == 0:
        print("\nGame over. You ran out of turns.")
        print(f"The correct number was {answer}.")

def main():
    print("Select difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Hard (5 attempts)")
    difficulty_choice = input("Enter your choice (1 or 2): ")

    if difficulty_choice == "1":
        play_game("easy")
    elif difficulty_choice == "2":
        play_game("hard")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()