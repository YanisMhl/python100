from turtle import Screen 
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

firstPaddle = Paddle(350, 0)
secondPaddle = Paddle(-350, 0)

screen.listen()
screen.onkey(firstPaddle.goUp, "Up")
screen.onkey(firstPaddle.goDown, "Down")
screen.onkey(secondPaddle.goUp, "z")
screen.onkey(secondPaddle.goDown, "s")
isGameOn = True 

while isGameOn:
    screen.update()


screen.exitonclick()