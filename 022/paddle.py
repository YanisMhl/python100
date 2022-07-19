from turtle import Turtle 

SPEED = 50

class Paddle(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x, y)
        
    
    def goUp(self):
        newY = self.ycor() + SPEED
        self.goto(self.xcor(), newY)
    
    def goDown(self):
        newY = self.ycor() - SPEED
        self.goto(self.xcor(), newY)
        

