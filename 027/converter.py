from tkinter import *

def calculateDistance():
    km = round(float(input.get()) * 1.6, 2) 
    km_lbl["text"] = f"is equal to {km} Km"

window = Tk() 
window.title("Mile to Km Converter")
window.minsize(width=500, height=200)

#Labels
miles_lbl = Label(text="Miles")
miles_lbl.grid(column=1, row=0)

km = 0
km_lbl = Label(text=f"is equal to {km} Km")
km_lbl.grid(column=0, row=1)

#Entry

input = Entry()
input.grid(column=0, row=0)

#Button
calculate_btn = Button(text="Calculate", command=calculateDistance)
calculate_btn.grid(column=0, row=2)


window.mainloop()