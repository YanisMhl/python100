from msilib.schema import Class
from turtle import Turtle 

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.goto(-50, 250)
        self.updateScoreboard()
        
    def updateScoreboard(self):
        self.write(f"Score : {self.score}", font=("Verdana", 15, "normal"))
        
    def gameOver(self):
        self.goto(-60, 0)
        self.write("GAME OVER", font=("Verdana", 15, "normal"))
    
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()