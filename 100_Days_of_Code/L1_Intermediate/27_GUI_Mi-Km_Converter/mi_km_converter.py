from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)

label_one = Label(text="is equal to", font=("Arial", 15, "bold"))
label_one.grid(column=0, row=1)

input = Entry()
input.grid(column=1, row=0)

label_two = Label(text="0", font=("Arial", 15, "bold"))
label_two.grid(column=1, row=1)

def calculate():
	result = str(int(input.get()) * 1.609)
	label_two.config(text=f"{result}")

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

label_three = Label(text="Miles", font=("Arial", 15, "bold"))
label_three.grid(column=2, row=0)

label_four = Label(text="Km", font=("Arial", 15, "bold"))
label_four.grid(column=2, row=1)

window.mainloop()