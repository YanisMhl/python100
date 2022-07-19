from turtle import Turtle 

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.updateScoreboard()
        
        
    def updateScoreboard(self):
        self.goto(-250, 250)
        self.write(f"Score : {self.score}", align="center", font=("Courier", 30, "normal"))


    def increaseScore(self):
        self.clear()
        self.score += 1
        self.updateScoreboard()
        
    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Courier", 30, "normal"))

    def youWin(self):
        self.goto(0, 0)
        self.write(f"You win !", align="center", font=("Courier", 30, "normal"))