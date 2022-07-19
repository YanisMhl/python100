import random
from turtle import Turtle, Screen 


#Turtle
t = Turtle()
t.speed(0)

colors = ["pink", "orange", "lime"]

for i in range(100):
    t.color(random.choice(colors))
    t.circle(100)
    t.setheading(t.heading() + 10)
    

#Screen
screen = Screen()
screen.exitonclick()