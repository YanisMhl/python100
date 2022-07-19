from calendar import c
from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lScore = 0
        self.rScore = 0
        self.updateScoreboard()


    def updateScoreboard(self):
        self.goto(-100, 200)
        self.write(self.lScore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rScore, align="center", font=("Courier", 80, "normal"))
    
    def leftPoint(self):
        self.lScore += 1
        self.clear()
        self.updateScoreboard()
        
    def rightPoint(self):
        self.rScore += 1
        self.clear()
        self.updateScoreboard()