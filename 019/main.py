import random
from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color:")

positions = [180, 60, -60, -180]

tim = Turtle()
tom = Turtle()
tam = Turtle()
tim.penup()
tom.penup()
tam.penup()
tim.goto(x=-240, y=random.choice(positions))
tom.goto(x=-240, y=random.choice(positions))
tam.goto(x=-240, y=random.choice(positions))


screen.exitonclick()