from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        upper = False
        if char.lower() in alphabet:
            if char not in alphabet:
                upper = True
            shifted_position = alphabet.index(char.lower()) + shift_amount
            shifted_position %= len(alphabet)
            if upper:
                output_text += alphabet[shifted_position].upper()
            else:
                output_text += alphabet[shifted_position]
        else:
            output_text += char
    print(f"Here is the {encode_or_decode}d result: {output_text}")


run_program = True

while run_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    run = input("Type 'yes' if you want to run it again. Otherwise, type 'no': ").lower()
    if run == 'no':
        run_program = False
        print("The program has ended.")
