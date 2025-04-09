from tkinter import *
import pandas
import random

#______________________ CONSTANTS __________________________________________________
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
polish_dict = {}

#______________________ CHANGE CARD _______________________________________________
try:
	words_dict = pandas.read_csv("unknown_words.csv")
except FileNotFoundError:
	original_data = pandas.read_csv("polish_frequency_list.csv")
	polish_dict = original_data.to_dict(orient="records")
else:
	#words_df = pandas.DataFrame(words_dict)
	polish_dict = words_dict.to_dict(orient="records")

def change_card():
	global flip_timer, current_card
	window.after_cancel(flip_timer)
	card.itemconfig(card_image, image=front_img)
	card.itemconfig(language, text="Polish", fill="black")
	current_card = random.choice(polish_dict)
	card.itemconfig(word, text=current_card["Polish"], fill="black")

	flip_timer = window.after(3000, flip_card)

def is_known():
	polish_dict.remove(current_card)
	data = pandas.DataFrame(polish_dict)
	data.to_csv("unknown_words.csv", index=False)
	change_card()

#______________________ FLIP CARD _________________________________________________
def flip_card():
	card.itemconfig(card_image, image=back_img)
	card.itemconfig(language, text="English", fill="white")
	card.itemconfig(word, text=current_card["English"], fill="white")

#______________________ UI CODE ____________________________________________________
window = Tk()
window.title("Polish Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
card_image = card.create_image(400, 263, image=front_img)
language = card.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = card.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)
back_img = PhotoImage(file="images/card_back.png")

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(column=1, row=1)

change_card()

window.mainloop()