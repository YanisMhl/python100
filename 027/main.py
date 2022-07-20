from tkinter import *

def buttonClicked():
    my_label.config(text=input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

#Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.grid(column=0, row=0)

#Button
button = Button(text="Click me bitch", command=buttonClicked)
button.grid(column=1, row = 1)

#New Button
newButton = Button(text="I'm a new button bitch")
newButton.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()