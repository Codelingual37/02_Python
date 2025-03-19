from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
	global reps
	reps = 0
	window.after_cancel(timer)
	canvas.itemconfig(timer_text, text=f"00:00")
	label.config(text="Timer", fg=GREEN)
	check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	global reps
	reps += 1

	work = 60 * WORK_MIN
	short_break = 60 * SHORT_BREAK_MIN
	long_break = 60 * LONG_BREAK_MIN
	if reps % 8 == 0:
		countdown(long_break)
		label.config(text="Break", fg=RED)
	elif reps % 2 == 0:
		countdown(short_break)
		label.config(text="Break", fg=PINK)
	else:
		countdown(work)
		label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
	count_min = math.floor(count / 60)
	count_sec = count % 60
	if count_sec < 10:
		count_sec = f"0{count_sec}"
	canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
	if count > 0:
		global timer
		timer = window.after(1000, countdown, count - 1)

	else:
		start_timer()
		marks = ""
		for i in range(math.floor(reps / 2)):
			marks += "✔"
		check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,  bg=YELLOW)

start_button = Button(text="Start", font=(FONT_NAME, 12, "normal"), command=start_timer)
start_button.grid(column=0, row=2)

label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_marks = Label(font=(FONT_NAME, 20, "normal"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"), command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()