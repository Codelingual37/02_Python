import tkinter

window = tkinter.Tk()
window.title("My First GUI rogram")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a label", font=("Arial", 25, "bold"))
label.pack()


window.mainloop()