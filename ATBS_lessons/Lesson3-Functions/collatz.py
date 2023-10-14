import sys


def collatzvar(number):
    while number != 1:
        if number % 2 == 0:
            newnum = number // 2
            print(newnum)
            return newnum
        elif number % 2 != 0:
            newnumodd = 3 * number + 1
            print(newnumodd)
            return newnumodd
        continue
try:
    num = int(input("Enter a number."))
except ValueError:
    print("Enter an integer")
while collatzvar != 1:        
    collatzvar(num)



