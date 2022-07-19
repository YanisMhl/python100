from turtle import Turtle

class Snake:
    
    def __init__(self):
        self.segments = []
        for i in range(0, 3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(i*-20, 0)
            self.segments.append(segment)
            
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
        self.segments[0].forward(20)