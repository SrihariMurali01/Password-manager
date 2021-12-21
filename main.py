from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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


# ---------------------------- SEARCH WEBSITE -------------------------------#
def find_password():
    website = website_e.get().upper()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Password Manager",
                            message="Welcome to Password Manager! Since this is the first time you are running this application, please add up to 1 entries!\n\n Have a great time!")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message="No details are available for the entered website.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    reply = None
    website = website_e.get()
    email = email_e.get()
    password = password_e.get()
    new_data = {
        website.upper(): {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!!")

    else:

        # TO CHECK IF A PREVIOUS ENTRY IS PRESENT.
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                if website in data:
                    reply = messagebox.askokcancel(title=website, message="It looks like there is previous entry for the entered website. Do you want to update the password?")
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        out = messagebox.askokcancel(title=website,
                                     message=f'These are the details entered: \nEmail: {email}\nPassword: {password} \nDo you wish to proceed with these details?')

        if out:
            messagebox.showinfo(title=website, message="Password saved successfully!")
            website_e.delete(0, END)
            password_e.delete(0, END)

    # APPLICABLE FOR BOTH UPDATE AND ADDING OF OLD AND NEW DETAILS RESPECTIVELY
    if reply:
        out = messagebox.askokcancel(title=website,
                                     message=f'These are the details entered: \nEmail: {email}\nPassword: {password} \nDo you wish to proceed with these details?')

        if out:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Updating new data
                    json.dump(data, data_file, indent=4)

            finally:
                messagebox.showinfo(title=website, message="Password saved successfully!")
                website_e.delete(0, END)
                password_e.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager v1.2")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_l = Label(text="Website:    ", font=FONT)
website_l.grid(column=0, row=1)
website_e = Entry()
website_e.focus()
website_e.config(width=37)
website_e.grid(column=1, row=1)
search_btn = Button(text="Search", borderwidth=1, command=find_password)
search_btn.grid(column=2, row=1)
search_btn.config(width=15)

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
