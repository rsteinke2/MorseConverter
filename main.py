
#prompt application for encoding and decoding morse code

#morse code dictionary
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def encode_in_morse():
    text = input("Type the text to convert: ").upper()
    morse_code = []

    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('')

    return ' '.join(morse_code)

#
def decode_to_text():
    morse_code = input("Type the Morse Code to convert: ")
    morse_words = morse_code.split('  ')  # Words are separated by 2 spaces (dits)
    decoded_text = []

    for morse_word in morse_words:
        morse_chars = morse_word.split()  # Characters are separated by 1 space
        decoded_word = ''.join([REVERSE_MORSE_DICT[char] for char in morse_chars])
        decoded_text.append(decoded_word)
    return ' '.join(decoded_text)

#index and main loop
while True:
    print("\n--------------- Morse Code Encoder and Decoder -------------\n")

    option = input("Choose your option:\n"
                   "Type [1] to convert Text => Morse Code\n"
                   "Type [2] to convert Morse Code => Text\n"
                   "Type [q] to quit\n")

    if option == '1':
        print(f"Your encoded message in Morse Code = {encode_in_morse()}")
    elif option == '2':
        print(f"Your decoded message = {decode_to_text()}")
    elif option.lower() == 'q':
        print("Exiting the program.")
        break
    else:
        print("Invalid option, please try again.")



