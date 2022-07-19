from turtle import Screen 
from player import Player
from car import Car
from carManager import CarManager
from scoreboard import Scoreboard
import time
import random


screen = Screen()
screen.setup(width=800, height=600)
screen.title("turtle crossing game")
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

isGameOn = True 

while isGameOn:
    time.sleep(0.1)
    screen.update()
    scoreboard.increaseScore()
    spawn = random.randint(0, 1)
    # if spawn == 1:
    #     carManager.createCars()
    if len(carManager.cars) > 0:
        for cars in carManager.cars:
            cars.move()
            #Detect collision with player 
            if player.distance(cars) < 20:
                scoreboard.gameOver()
                isGameOn = False
    
    #Win?
    if player.ycor() >= 280:
        scoreboard.youWin()
        isGameOn = False
            

    
screen.exitonclick()