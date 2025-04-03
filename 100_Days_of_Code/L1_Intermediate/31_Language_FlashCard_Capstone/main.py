from tkinter import *
import pandas
import random

#______________________ CONSTANTS __________________________________________________
BACKGROUND_COLOR = "#B1DDC6"

#______________________ FILL CARDS _________________________________________________
words_dict = pandas.read_csv("polish_frequency_list.csv")
words_df = pandas.DataFrame(words_dict)
polish_dict = words_df.to_dict(orient="records")

def change_card():
	card_front.itemconfig(language, text="Polish")
	current_card = random.choice(polish_dict)
	card_front.itemconfig(word, text=current_card["Polish"])

#______________________ UI CODE ____________________________________________________
window = Tk()
window.title("Polish Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
card_front.create_image(400, 263, image=front_img)
language = card_front.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = card_front.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card_front.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_card)
right_button.grid(column=1, row=1)

change_card()

window.mainloop()