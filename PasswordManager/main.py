from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip
import tkinter
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for n in range(randint(8, 10))]
    password_symbols = [choice(symbols) for n in range(randint(2, 4))]
    password_numbers = [choice(numbers) for n in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def dump_json(data, data_file):
    json.dump(data, data_file, indent=4)


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
        except FileNotFoundError:
            data = new_data
            with open("data.json", "w") as data_file:
                # Saving updated data
                dump_json(data, data_file)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                dump_json(data, data_file)
        finally:
            website_input.delete(0, "end")
            password_input.delete(0, "end")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def find_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website} Password", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {website}.")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
pass_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = tkinter.Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

website_search = tkinter.Button(text="Search", command=find_password)
website_search.grid(column=2, row=1)

email_user_label = tkinter.Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

email_input = tkinter.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "amy.nguyen@gmail.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = tkinter.Entry(width=21)
password_input.grid(column=1, row=3)

password_button = tkinter.Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
