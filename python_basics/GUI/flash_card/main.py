from tkinter import *
import pandas as pd
import random

# ---------------------------- DATA SETUP ------------------------------- #

try:
    data = pd.read_csv("data/french_words.csv")
    word_list = data.to_dict(orient="records")
except FileNotFoundError:
    word_list = []

current_card = {}
flip_timer = None

# ---------------------------- UI SETUP ------------------------------- #

# Create window
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg="#B1DDC6")

# Load images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# Canvas for flashcard
display_canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
card_background = display_canvas.create_image(400, 263, image=card_front_img)
title_text = display_canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word_text = display_canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
display_canvas.grid(row=0, column=0, columnspan=2)

# Functions
def flip_card():
    display_canvas.itemconfig(card_background, image=card_back_img)
    display_canvas.itemconfig(title_text, text="English", fill="white")
    display_canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def next_card():
    global current_card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    
    current_card = random.choice(word_list)
    display_canvas.itemconfig(card_background, image=card_front_img)
    display_canvas.itemconfig(title_text, text="French", fill="black")
    display_canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    
    flip_timer = window.after(3000, flip_card)

def is_known():
    word_list.remove(current_card)
    next_card()

def is_unknown():
    next_card()

wrong_button = Button(image=wrong_img, highlightthickness=0, command=is_unknown)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
