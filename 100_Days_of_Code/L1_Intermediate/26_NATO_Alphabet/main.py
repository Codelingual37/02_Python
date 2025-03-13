import pandas

nato_dict = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(nato_dict)
code_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

user_word = input("Please enter a word: ").upper()
code_list = [code_dict[letter] for letter in user_word]

# Alternative but wordier way
# code_list = [value for letter in user_word for (key, value) in code_dict.items() if letter == key]
print(code_list)
