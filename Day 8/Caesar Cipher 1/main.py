alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

# TODO-1
def encrypt(original_text, shift_amount):
    # shift each letter of the 'original_text' forwards in the alphabet
    encoded_text = ''
    for char in original_text:
        # debug print - to check the correct value on the alphabet array
        # print(f"The letter {char} is the {alphabet.index(char)}, i.e. {alphabet[alphabet.index(char)+shift_amount]}")
        # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        # doing some check to avoid the error list index out of range -> module function
        if alphabet.index(char)+shift_amount> 25:
            shifted = (alphabet.index(char)+shift_amount) % len(alphabet)
        else:
            shifted = alphabet.index(char)+shift_amount
        encoded_text += alphabet[shifted]
    print(f"This is the encoded text: {encoded_text}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs.
encrypt(text, shift)

