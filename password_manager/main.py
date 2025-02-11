from tkinter import *
from tkinter import messagebox
import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if not website or not email or not password:
        messagebox.showwarning(title="Warning", message="Please fill in all fields.")
        return
    
    is_ok = messagebox.askokcancel(title="Confirm", message=f"Save the following details?\n\nWebsite: {website}\nEmail: {email}\nPassword: {password}")
    
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
        
        website_entry.delete(0, END)
        password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

# Label
website_label = Label(text="Website")
website_label.grid(row=1, column=0, sticky="ew")

email_label = Label(text="Email")
email_label.grid(row=2, column=0, sticky="ew")

password_label = Label(text="Password")
password_label.grid(row=3, column=0, sticky="ew")

# Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0, "briankim129@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

# Button
generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=0, columnspan=3, sticky="ew")

window.mainloop()
