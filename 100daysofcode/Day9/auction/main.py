from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

def auction():
    while True:
        auctiondict = {}
        print(art.logo)
        #Ask for inputs
        name = input("What is your name?\n")
        bid = input("What is your bid price?\n")
        #Add to dict
        auctiondict[name] = bid
        ask = input("Are there any others who would like to bid?").lower()
        if ask == 'yes':
            clear()
            continue
        elif ask == 'no':
            highest_bid = max(auctiondict.values())
            print("The highest bid is:", highest_bid)
            break
        
auction()
        