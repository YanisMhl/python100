import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=800)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessedStates = []

while len(guessedStates) < 50:
    answerState = screen.textinput(title=f"{len(guessedStates)}/50 States Correct", prompt="What's another state's name ?")
    if answerState == "exit":
        break
    for i in range(len(states)):
        if answerState.lower() == states[i].lower():
            guessedStates.append(answerState)
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(data["x"][i], data["y"][i])
            t.write(states[i])
        

statesCsv = pandas.DataFrame(states)
statesCsv.to_csv("statesToLearn.csv")