#import anothermodule
#print(anothermodule.another_variable)

#import turtle


# from turtle import Turtle, Screen

# timmy = Turtle() #initialize or construct on object from the blueprint
# print(timmy)
# timmy.shape("turtle")
# timmy.color('red')
# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charzard", "Squirtle"])
table.add_column("Type", ["Electirc", "Water", "Fire"])
table.align = "l"
print(table)
