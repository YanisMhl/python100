import random
import colorgram
from turtle import Turtle, Screen, colormode 

colormode(255)

colors = colorgram.extract('image.jpg', 20)

#turtle
t = Turtle()
color = random.choice(colors).rgb
t.color(color)
t.dot(5)
t.penup()
t.forward(100)

#Screen
screen = Screen()
screen.exitonclick()