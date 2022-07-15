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

screen.exitonclick()