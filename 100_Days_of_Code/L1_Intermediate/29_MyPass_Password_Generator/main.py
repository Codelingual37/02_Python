from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	nr_letters = random.randint(8, 10)
	nr_symbols = random.randint(2, 4)
	nr_numbers = random.randint(2, 4)

	password_letters = [random.choice(letters) for char in range(nr_letters)]
	password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
	password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

	password_list = password_letters + password_symbols + password_numbers

	random.shuffle(password_list)

	password = "".join(password_list)
	password_input.insert(0, password)
	pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website = website_input.get()
	email_user = email_user_input.get()
	password = password_input.get()

	if len(website) == 0:
		return messagebox.showwarning(title="Missing Information", message="Please enter a website.")
	elif len(password) == 0:
		return messagebox.showwarning(title="Missing Information", message="Please enter the password.")
	else:
		is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_user} "
							f"\nPassword: {password}\nIs it okay to save?")
		
		if is_ok:
			with open("data.txt", "a+") as new:
				new.write(f"{website} | {email_user} | {password}\n")
			website_input.delete(0, END)
			password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_user = Label(text="Email/Username:")
email_user.grid(column=0, row=2)

email_user_input = Entry(width=40)
email_user_input.grid(column=1, row=2, columnspan=2)
email_user_input.insert(0, "fakeemail@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()