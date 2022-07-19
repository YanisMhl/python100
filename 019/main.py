<<<<<<< HEAD
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)
    
def rotate_left():
    tim.left(20)

def rotate_right():
    tim.right(20)
    
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="z", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="q", fun=rotate_left)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="c", fun=clear)
=======
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

>>>>>>> 311f7f7eefcc19654d479c9eb002b6af451e2668

screen.exitonclick()