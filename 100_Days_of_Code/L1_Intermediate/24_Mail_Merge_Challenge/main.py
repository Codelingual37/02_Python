with open("Input/Letters/starting_letter.txt") as letter:
	template = letter.read()
	
with open("Input/Names/invited_names.txt") as list:
	names = list.readlines()

for name in names:
	stripped = name.strip()
	template = template.replace("[name]", stripped)
	with open(f"Output/ReadyToSend/letter_for_{stripped}.docx", mode="w") as new:
		new_letter = new.write(template)
	template = template.replace(stripped, "[name]")
	