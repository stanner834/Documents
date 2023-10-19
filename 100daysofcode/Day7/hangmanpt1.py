import random
word_list = ["advark", "baboon", "camel"]
random_word = random.choice(word_list)
counter = 0

guesscount = 5
for i in range(1,6):
    try:
        guess_word = input(f"Guess a letter.\n").lower()
        if guess_word in random_word:
            print("Congrats! Correct letter.")
        elif guess_word != random_word:
            counter += 1
            print(f"Try again! you have {guesscount - counter} tries left.")
    except:
        print("Wrong input, try again!")
