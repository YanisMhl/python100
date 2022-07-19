from turtle import Turtle

startingPositions = [(0, 0), (-20, 0), (-40, 0)]
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
        for position in startingPositions:
            self.addSegment(position)
            
            
    def addSegment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
        
    def extend(self):
        self.addSegment(self.segments[-1].position())
        
        
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
            
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.createSnake()
        self.head = self.segments[0]