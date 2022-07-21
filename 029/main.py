from tkinter import *
from tkinter import messagebox
from os.path import exists
from typing import final
from password import PasswordGenerator
from random import randint
import json 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def passwordGeneration():
    p = PasswordGenerator(randint(5,7), randint(2,4), randint(2,4))
    p.generate()
    passwordEntry.delete(0, END)
    passwordEntry.insert(0, p.password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def saveData():
    
    website = websiteEntry.get()
    id = userInfoEntry.get()
    password = passwordEntry.get()
    
    newData = {
        website:{
            "email": id,
            "password":password,
        }
    }
    
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {id}\nPassword: {password}\nIs it ok to save?")  
        if is_ok:
                try:
                    with open("password.json", mode="r") as file:
                        #Reading old data
                        data = json.load(file)
                except FileNotFoundError:
                    with open("password.json", mode="w") as file:
                        json.dump(newData, file, indent=4)
                else:
                    #Updating old data with new data
                    data.update(newData)
                    with open("password.json", mode="w") as file:
                        #Saving updated data
                        json.dump(data, file, indent=4)
                finally:
                    websiteEntry.delete(0, END)
                    passwordEntry.delete(0, END)        
                    
# ---------------------------- SEARCH DATA ------------------------------- #

def searchData():
    website = websiteEntry.get()
    try:
        with open("password.json", mode="r") as file:
            data = json.load(file)
            try:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            except KeyError:
                messagebox.showinfo(title="Website not found", message="Sorry there is no data for this website.")
            
    except FileNotFoundError:
        messagebox.showinfo(title="File missing error", message="Sorry there is no data.")
    
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
websiteEntry = Entry(width=25)
websiteEntry.grid(column=1, row=1)
websiteEntry.focus()
userInfoEntry = Entry(width=50)
userInfoEntry.grid(column=1, row=2, columnspan=2)
userInfoEntry.insert(0, "random@gmail.com")
passwordEntry = Entry(width=25)
passwordEntry.grid(column=1, row=3)

#Buttons
passwordBtn = Button(text="Generate Password", width=15, command=passwordGeneration)
passwordBtn.grid(column=2, row=3)
addBtn = Button(text="Add", width=36, command=saveData)
addBtn.grid(column=1, row=4, columnspan=2)
searchBtn = Button(text="Search", width=15, command=searchData)
searchBtn.grid(column=2, row=1)


window.mainloop()