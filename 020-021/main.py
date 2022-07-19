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

gameIsOn = True 

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    

screen.exitonclick()