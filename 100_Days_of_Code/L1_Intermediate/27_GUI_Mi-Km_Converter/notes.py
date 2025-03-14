from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = Label(text="I am a label", font=("Arial", 25, "bold"))
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

def button_clicked():
	label.config(text=f"{input.get()}")

button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click Me!", command=button_clicked)
button2.grid(column=2, row=0)

input = Entry()
input.grid(column=3, row=2)

window.mainloop()