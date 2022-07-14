from turtle import Turtle, Screen



turtle = Turtle()

for i in range(100):
    if i % 2 == 0:
        turtle.penup()
    else:
        turtle.pendown()
    turtle.forward(2)





#screen
screen = Screen()
screen.exitonclick()