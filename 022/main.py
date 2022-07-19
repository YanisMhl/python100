from turtle import Screen 
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

firstPaddle = Paddle(350, 0)
secondPaddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(firstPaddle.goUp, "Up")
screen.onkey(firstPaddle.goDown, "Down")
screen.onkey(secondPaddle.goUp, "z")
screen.onkey(secondPaddle.goDown, "s")
isGameOn = True 

while isGameOn:
    time.sleep(0.03)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
        
    if ball.distance(firstPaddle) < 50 and ball.xcor() > 340:
        ball.bounceX()
        scoreboard.leftPoint()
        
    if ball.distance(secondPaddle) < 50 and ball.xcor() < -340:
        ball.bounceX()
        
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.resetPosition()
        scoreboard.rightPoint()

screen.exitonclick()