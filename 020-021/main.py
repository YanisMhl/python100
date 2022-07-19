import random 
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()
        
    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameIsOn = False 
        scoreboard.gameOver()
        
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameIsOn = False 
            scoreboard.gameOver()

screen.exitonclick()