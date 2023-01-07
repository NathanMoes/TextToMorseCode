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
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    to_translate = input("Please enter the text to translate\n")
    translated_code = []
    outPutText = ''
    for char in to_translate:
        if char != ' ':
            translated_code.append(MORSE_CODE_DICT[char.upper()])
        else:
            translated_code.append(' ')
    for code in translated_code:
        outPutText += code + ' '
    print("translated morse code:\n" + outPutText)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
