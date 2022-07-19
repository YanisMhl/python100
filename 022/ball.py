from turtle import Turtle 


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.Xmove = 5
        self.Ymove = 5

    def move(self):
        newX = self.xcor() + self.Xmove
        newY = self.ycor() + self.Ymove
        self.goto(newX, newY)
        
    def bounceY(self):
        self.Ymove *= -1

    def bounceX(self):
        self.Xmove *= -1
        
    def resetPosition(self):
        self.goto(0, 0)