import pandas

nato_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(nato_dict)
code_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

invalid_input = True

while invalid_input:
	user_word = input("Please enter a word: ").upper()
	try:
		code_list = [code_dict[letter] for letter in user_word]
	except KeyError:
		print("Sorry, only letters in the alphabet, please.")
	else:
		invalid_input = False

# Alternative but wordier way
# code_list = [value for letter in user_word for (key, value) in code_dict.items() if letter == key]
print(code_list)
