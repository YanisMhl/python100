from turtle import Turtle
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]   
        
    def createSnake(self):
        for i in range(0, 3):
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(i*-20, 0)
            self.segments.append(segment)
        
        
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
        self.head.forward(SPEED)
    
    def goUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def goDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def goLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def goRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)