import random
from turtle import Turtle, Screen

colors = ["orange", "blue", "red", "green", "lime", "pink", "brown", "indigo", "silver", "yellow"]

def drawShape(turt, numberOfSides, angle):
    color = random.choice(colors)
    colors.remove(color)
    turt.color(color)
    for i in range(numberOfSides):
        turt.forward(100) 
        turt.right(angle)



turtle = Turtle()

#triangle
drawShape(turtle, 3, 120)
#square
drawShape(turtle, 4, 90)
#pentagon
drawShape(turtle, 5, 72)
#hexagon
drawShape(turtle, 6, 60)
#heptagon
drawShape(turtle, 7, 51.5)
#octagon
drawShape(turtle, 8, 45)
#nonagon
drawShape(turtle, 9, 40)
#decagon
drawShape(turtle, 10, 36)


#Screen stuff
screen = Screen()
screen.exitonclick()