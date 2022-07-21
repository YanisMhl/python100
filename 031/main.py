from tkinter import *
from tkinter import messagebox
import pandas 
import csv 
import random

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 526

data = pandas.read_csv("data/french_words.csv")

frenchLanguage = data.columns[0]
englishLanguage = data.columns[1]

frenchWords = data["French"].to_list()
englishWords = data["English"].to_list()


frenchWord = random.choice(frenchWords)
englishWord = englishWords[frenchWords.index(frenchWord)]
frenchWords.remove(frenchWord)
englishWords.remove(englishWord)
#----------CREATE NEW FLASH CARDS----------#

def randomWords():
    global frenchWords
    global frenchWord
    global englishWords
    global englishWord
    try:
        frenchWord = random.choice(frenchWords)
        englishWord = englishWords[frenchWords.index(frenchWord)]
        frenchWords.remove(frenchWord)
        englishWords.remove(englishWord)
        canvas.itemconfig(wordTxt, text=frenchWord)
        print(englishWord)
    except:
        messagebox.showinfo(title="End of the game", message="Sorry ! There is no more words to learn.\n You finished the game!")
        

#window setup

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
frontCardImg = PhotoImage(file="images/card_front.png")
backCardImg = PhotoImage(file="images/card_back.png")
canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=frontCardImg)
languageTxt = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
wordTxt = canvas.create_text(400, 263, text=frenchWord, fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=1, row=0)


#Buttons
rightImg = PhotoImage(file="images/right.png")
wrongImg = PhotoImage(file="images/wrong.png")
rightBtn = Button(image=rightImg, highlightthickness=0, command=randomWords)
wrongBtn = Button(image=wrongImg, highlightthickness=0, command=randomWords)
rightBtn.grid(column=2, row=1)
wrongBtn.grid(column=0, row=1)







window.mainloop()