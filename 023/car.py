from turtle import Turtle
import random

colors = ["red", "orange", "purple", "blue", "green"]

class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(400, random.randint(-280, 280))
        self.speed = random.randint(10, 20)

                
    def move(self):
        newX = self.xcor() - self.speed
        self.goto(newX, self.ycor())