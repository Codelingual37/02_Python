#FileNotFound
# try:
# 	file = open("a_file.txt")
# 	a_dict = {"key": "value"}
# 	print(a_dict["asdiojfod"])
# except FileNotFoundError:
# 	file = open("a_file.txt", "w")
# 	file.write("something")
# except KeyError as error_message:
# 	print(f"The key {error_message} does not exist.")
# else:
# 	content = file.read()
# 	print(content)
# finally:
# 	file.close()
# 	print("File was closed.")

height = float(input("height: "))
weight = float(input("weight: "))

if height > 3:
	raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
