alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text, shift_amount):
    # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
    #  by the shift amount and print the decrypted text.
    decrypted_text = ''
    for letter in original_text:
        shift_back_position = alphabet.index(letter) - shift_amount
        shift_back_position %= len(alphabet)
        decrypted_text += alphabet[shift_back_position]
    print(f"Here is the decoded result: {decrypted_text}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
# def caesar(function, original_text, shift_amount):
#     if function == "encode":
#         encrypt(original_text=text, shift_amount=shift)
#     elif function == "decode":
#         decrypt(original_text=text, shift_amount=shift)
#     else:
#         print("Ops, something wrong! Please try again..")

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

# encrypt(original_text=text, shift_amount=shift)

# caesar(direction,text,shift)

# another way to write the caesar function
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(original_text, shift_amount, encode_decode):
    output_text = ""
    if encode_decode == "encode":
        shift_amount = shift_amount * 1
    elif encode_decode == "decode":
        shift_amount = -1 * shift_amount
    else:
        print("Ops, something wrong! Please try again..")
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_decode}d result: {output_text}")

caesar(encode_decode=direction, original_text=text, shift_amount=shift)



