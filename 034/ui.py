from tkinter import * 

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.scoreLbl = Label(text="Score : 0", fg="white", bg=THEME_COLOR)
        self.scoreLbl.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.questoin_text = self.canvas.create_text(150, 125, text="Some question text", fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2)
        
        
        self.window.mainloop()