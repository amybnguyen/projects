from tkinter import Button, Canvas, PhotoImage, Tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

current_card = {}

# --------------------- GET DATA ------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


# --------------------- FLIP CARD ------------------- #
def flip_card():
    global current_card
    canvas.itemconfig(card_color, image=flashcard_image_b)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_color, image=flashcard_image_f)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    window.after(3000, flip_card)


def is_known():
    global current_card
    to_learn.remove(current_card)
    new_to_learn = pandas.DataFrame(to_learn)
    new_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# --------------------- UI SETUP ------------------- #
# Create Window
window = Tk()
window.title("Flashy")
window.minsize(200, 200)
window.config(bg=BACKGROUND_COLOR,padx=50, pady=50)

# Import images
flashcard_image_f = PhotoImage(file="images/card_front.png")
flashcard_image_b = PhotoImage(file="images/card_back.png")
x_image = PhotoImage(file="images/wrong.png")
check_image = PhotoImage(file="images/right.png")

# Grid
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_color = canvas.create_image(400, 263, image=flashcard_image_f)
card_title = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)
next_card()

x_button = Button(image=x_image, highlightthickness=0, command=next_card)
x_button.grid(column=0, row=1)

check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(column=1, row=1)

window.mainloop()
