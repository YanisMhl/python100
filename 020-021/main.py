import random 
import time
from snake import Snake
from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()

screen.onkey(snake.goUp, "Up")
screen.onkey(snake.goDown, "Down")
screen.onkey(snake.goLeft, "Left")
screen.onkey(snake.goRight, "Right")


gameIsOn = True 
while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    

screen.exitonclick()