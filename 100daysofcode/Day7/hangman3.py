import random
userlist = []
word_list = ["advark", "baboon", "camel"]
choose_word = random.choice(word_list)
count = 0
while count <= 5:
    guess = input("Guess a letter!").lower()
    for letter in choose_word:
        if letter == guess:
            userlist.append(guess)
        if letter not in guess:
            userlist.append("_") #append does not work
            
        result = ' '.join(userlist)
    count += 1
    print(result)


