import random
from turtle import Turtle, Screen 

colors = ["cornflower blue", "teal", "peach puff","light green", "purple"]

turtle = Turtle()
turtle.speed(0)
directions = [0, 90, 180, 270]


for i in range(1000):
    turtle.color(random.choice(colors))
    turtle.pensize(random.randint(5, 10))
    turtle.forward(random.randint(20, 60))
    turtle.right(random.choice(directions))


#Screen
screen = Screen()
screen.exitonclick()