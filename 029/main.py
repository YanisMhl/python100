from tkinter import *
from tkinter import messagebox
from os.path import exists
from password import PasswordGenerator
from random import randint
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def passwordGeneration():
    p = PasswordGenerator(randint(5,7), randint(2,4), randint(2,4))
    p.generate()
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, p.password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def addCurrentAccount():
    saveData(websiteEntry.get(), userInfoEntry.get(), passwordEntry.get())

def saveData(website, id, password):
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {id}\nPassword: {password}\nIs it ok to save?")  
        if is_ok:
            if not exists("password.txt"):
                with open("password.txt", mode="w") as file:
                    file.write(f"{website} | {id} | {password}\n")
            else:
                with open("password.txt", mode="a") as file:
                    file.write(f"{website} | {id} | {password}\n")
                
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)              
    
# ---------------------------- UI SETUP ------------------------------- #

#Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=15, pady=15)

#Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website: ")
website.grid(column=0, row=1)
userInfo = Label(text="Email/Username: ")
userInfo.grid(column=0, row=2)
password = Label(text="Password: ")
password.grid(column=0, row=3)

#Entries
websiteEntry = Entry(width=35)
websiteEntry.grid(column=1, row=1, columnspan=2)
websiteEntry.focus()
userInfoEntry = Entry(width=35)
userInfoEntry.grid(column=1, row=2, columnspan=2)
userInfoEntry.insert(0, "random@gmail.com")
passwordEntry = Entry(width=21)
passwordEntry.grid(column=1, row=3)

#Buttons
passwordBtn = Button(text="Generate Password", command=passwordGeneration)
passwordBtn.grid(column=2, row=3)
addBtn = Button(text="Add", width=36, command=addCurrentAccount)
addBtn.grid(column=1, row=4, columnspan=2)



window.mainloop()