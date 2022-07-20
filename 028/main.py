from tkinter import *
from tracemalloc import start
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_lbl.config(text="timer")
    check_lbl.config(text="")
    global reps
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def startTimer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countDown(long_break_sec)
        timer_lbl.config(text="break")
    elif reps % 2 == 0:
        countDown(short_break_sec)
        timer_lbl.config(text="break")
    else:
        countDown(work_sec)
        timer_lbl.config(text="work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds < 10:
        seconds = f"0{seconds}"
    
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count-1)
    else:
        startTimer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✅" 
        check_lbl.config(text="mark")
        
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas et Images
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#Labels
timer_lbl = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer_lbl.grid(column=1, row=0)

check_lbl = Label(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
check_lbl.grid(column=1, row=3)

#Buttons
start_btn = Button(text="Start", highlightthickness=0, command=startTimer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", highlightthickness=0, command=resetTimer)
reset_btn.grid(column=2, row=2)


window.mainloop()