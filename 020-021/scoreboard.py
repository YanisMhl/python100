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
        with open("highscore.txt", mode="r") as file:
            self.highScore = int(file.read())
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.highScore}", font=("Verdana", 15, "normal"))
        
    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highScore))
        self.score = 0
        self.updateScoreboard()
    
    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()