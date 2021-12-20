import os
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = ("Arial", 12, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    let = [random.choice(letters) for _ in range(nr_letters)]
    sym = [random.choice(symbols) for _ in range(nr_symbols)]
    num = [random.choice(numbers) for _ in range(nr_numbers)]

    pwd = let + sym + num
    pwd = ''.join(random.sample(pwd, len(pwd)))

    password_e.insert(0, pwd)
    pyperclip.copy(pwd)
    messagebox.showinfo(title=website_e.get(), message="Password copied to clipboard!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_e.get()
    email = email_e.get()
    password = password_e.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!!")

    else:
        out = messagebox.askokcancel(title=website,
                                     message=f'These are the details entered: \nEmail: {email}\nPassword: {password} \nDo you wish to proceed with these details?')

        if out:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}    |    {email}   |    {password}\n")
                website_e.delete(0, END)
                password_e.delete(0, END)
                messagebox.showinfo(title=website, message="Password saved successfully in \"data.txt\"")
                os.startfile("data.txt")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_l = Label(text="Website:    ", font=FONT)
website_l.grid(column=0, row=1)
website_e = Entry()
website_e.focus()
website_e.config(width=55)
website_e.grid(column=1, row=1, columnspan=2)

email_l = Label(text="Email/Username:    ", font=FONT)
email_l.grid(column=0, row=2)
email_e = Entry()
email_e.insert(0, "sriharisai6230@gmail.com")
email_e.config(width=55)
email_e.grid(column=1, row=2, columnspan=2)

password_l = Label(text="Password:      ", font=FONT)
password_l.grid(column=0, row=3)
password_e = Entry()
password_e.config(width=37)
password_e.grid(column=1, row=3)
password_btn = Button(text="Generate Password", borderwidth=1, command=generate_password)
password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", borderwidth=5, command=save)

add_btn.config(width=45)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
