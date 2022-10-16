from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# TODO 1 Creating a UI
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 130, text="Title", font=("Ariel", 30, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 45, "bold"))
canvas.grid(column=0, row=0, columnspan=5, rowspan=3)

# TODO 2 Reading csv file and generating word pairs
# working with data
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
pair = {}


# function to draw random cards
def next_card():
    global pair, flip_timer
    window.after_cancel(flip_timer)
    pair = random.choice(to_learn)
    fr_word = pair["French"]
    canvas.itemconfig(word, text=fr_word, fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)

    flip_timer = window.after(3000, flip_card)


# TODO 3 Flip the card after 3 sec

def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    en_word = pair["English"]
    canvas.itemconfig(title, fill="white", text="English")
    canvas.itemconfig(word, fill="white", text=en_word, )


flip_timer = window.after(3000, func=flip_card)

# Buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(column=3, row=4)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=4)

next_card()

window.mainloop()
