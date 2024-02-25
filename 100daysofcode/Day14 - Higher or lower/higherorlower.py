import random

class HighLowGame:
    def __init__(self):
        self.score = 0
        self.names = ["John", "Mary", "David", "Jennifer", "James", "Patricia", "Michael", "Linda", "William", "Elizabeth", "Daniel", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Christopher", "Nancy"]  # Add more names as needed
        self.followers = {}
        for name in self.names:
            self.followers[name] = random.randint(0, 1000000)  # Assign a random follower count
        print(self.followers)
    def play_round(self):
        # Create a list of remaining players
        remaining_players = list(self.followers.keys())
        
        # Randomly select the first player from the remaining players
        player_a = random.choice(remaining_players)
        remaining_players.remove(player_a)  # Remove player_a from the list
        
        # Randomly select the second player from the updated list of remaining players
        player_b = random.choice(remaining_players)
        
        # Display the followers count for the selected players
        print("{} has {} followers.".format(player_a, self.followers[player_a]))
        print("{} has {} followers.".format(player_b, self.followers[player_b]))

        # Ask the user to guess who has more followers
        guess = input("Who has more Instagram followers, {} or {}? ".format(player_a, player_b)).strip().lower()

        # Determine the correct answer
        if self.followers[player_a] > self.followers[player_b]:
            correct_answer = "a"
        else:
            correct_answer = "b"

        # Check if the user's guess is correct
        if guess == correct_answer:
            print("Congratulations! You guessed correctly.")
            self.score += 1
            return True  # Return True if the user guessed correctly
        else:
            print("Sorry, that's incorrect.")
            return False  # Return False if the user guessed incorrectly

    def play_game(self):
        while True:
            if not self.play_round():  # If the user loses, exit the loop
                print("Your final score is {}.".format(self.score))
                print("Thanks for playing!")
                break
            else:
                print("Your current score is {}.".format(self.score))

if __name__ == "__main__":
    game = HighLowGame()
    game.play_game()

