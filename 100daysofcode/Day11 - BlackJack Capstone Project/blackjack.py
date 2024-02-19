import random
import art
import sys
cards = [11, 2,3,4,5,6,7,8,9,10,10,10,10]


def deal_cards():
    while True:
        usrcards = []
        compcards= []
        usrcards.extend(random.choices(cards, k =2))
        compcards.extend(random.choices(cards, k=2))
        
        usr_sum = sum(usrcards)
        comp_sum = sum(compcards)

        if usr_sum == 21:
            print(f"Your cards: {usrcards}, current score: {usr_sum}")
            print(f"Computers first card: {compcards[0]}")
            print("User BlackJack!")
            userinp = input("Type 'y' to get play again, type 'q' to quit: ")
            if userinp == 'y':
                continue
            elif userinp =='q':
                print("Exitting")
                break
        flag = True
        while flag:
            print(art.logo)
            print(f"Your cards: {usrcards}, current score: {usr_sum}")
            print(f"Computers first card: {compcards[0]}")
            userinp = input("Type 'y' to get another card, type 'n' to pass: ")
            if userinp == 'y':
                usrcards.extend(random.choices(cards, k = 1))
                usr_sum = sum(usrcards)
                if usr_sum > 21:
                    print(f"Your cards: {usrcards}, final score: {usr_sum}")
                    print(f"Computers cards: {compcards}, score: {comp_sum}")
                    print("YOU LOSE!")
                    userinp = input("Type 'y' to get play again, type 'q' to quit: ")
                    if userinp == 'y':
                        deal_cards()
                    elif userinp =='q':
                        print("Exitting")
                        sys.exit()
                elif usr_sum == 21:
                    print(f"Your cards: {usrcards}, final score: {usr_sum}")
                    print(f"Computers cards: {compcards}, score: {comp_sum}")
                    print("BLACKJACK!")
                    userinp = input("Type 'y' to get play again, type 'q' to quit: ")
                    if userinp == 'y':
                        deal_cards()
                    elif userinp =='q':
                        print("Exitting")
                        sys.exit()
                else:
                    continue
            elif userinp =='n':
                while comp_sum < 16:
                    compcards.extend(random.choices(cards, k=1))
                    comp_sum = sum(compcards)
                if comp_sum > 21:
                    print(f"Your cards: {usrcards}, final score: {usr_sum}")
                    print(f"Computers cards: {compcards}, score: {comp_sum}")
                    print("You win!")
                    userinp = input("Type 'y' to get play again, type 'q' to quit: ")
                    if userinp == 'y':
                        deal_cards()
                    elif userinp =='q':
                        print("Exitting")
                        sys.exit()
                elif usr_sum > comp_sum:
                    print(f"Your cards: {usrcards}, final score: {usr_sum}")
                    print(f"Computers cards: {compcards}, score: {comp_sum}")
                    print("You win!")
                    userinp = input("Type 'y' to get play again, type 'q' to quit: ")
                    if userinp == 'y':
                        deal_cards()
                    elif userinp =='q':
                        print("Exitting")
                        sys.exit()
                elif usr_sum == comp_sum:
                    print(f"Your cards: {usrcards}, final score: {usr_sum}")
                    print(f"Computers cards: {compcards}, score: {comp_sum}")
                    print("TIE!")
                    userinp = input("Type 'y' to get play again, type 'q' to quit: ")
                    if userinp == 'y':
                        deal_cards()
                    elif userinp =='q':
                        print("Exitting")
                        sys.exit()
                elif comp_sum == 21 and comp_sum > usr_sum:
                    print(f"Your cards: {usrcards}, final score: {usr_sum}")
                    print(f"Computers cards: {compcards}, score: {comp_sum}")
                    print("Comp!")
                    userinp = input("Type 'y' to get play again, type 'q' to quit: ")
                    if userinp == 'y':
                        deal_cards()
                    elif userinp =='q':
                        print("Exitting")
                        sys.exit()
                        
inp = input("Do you want to play a game of blackJack? ('y' or 'n'): ").lower()
if inp == 'y':
    deal_cards()    