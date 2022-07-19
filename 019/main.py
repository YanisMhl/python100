import random
from turtle import Turtle, Screen 

isRaceOn = False
screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yPositions = [-70, -40, -10, 20, 50, 80]
allTurtles = []
for i in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[i])
    newTurtle.penup()
    newTurtle.goto(x=-230, y=yPositions[i])
    allTurtles.append(newTurtle)

if userBet:
    isRaceOn = True
    
while isRaceOn:
    for t in allTurtles:
        if t.xcor() > 230:
            isRaceOn = False
            winningColor = t.pencolor()
            if winningColor == userBet:
                print(f"You've won! The {winningColor} turtle is the winner !")
            else:
                print(f"You've lost. The {winningColor} turtle is the winner.")
                
        randDistance = random.randint(0, 10)
        t.forward(randDistance)
    

screen.exitonclick()