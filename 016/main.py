from turtle import Turtle, Screen 
from prettytable import PrettyTable

# #Turtle
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.forward(150)
# timmy.color("green")
#Display
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

