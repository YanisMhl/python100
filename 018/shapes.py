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

def drawAllShapes(turt):
    for i in range(3, 11):
        drawShape(turt, i, 360/i)


turtle = Turtle()
drawAllShapes(turtle)



#Screen stuff
screen = Screen()
screen.exitonclick()