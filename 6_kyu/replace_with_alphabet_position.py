# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
    alpha_list = list()

    for letter in text.lower():
        letter_ord = ord(letter)
        if letter_ord >= ord('a') and letter_ord <= ord('z'):
            alpha_list.append(str(letter_ord - 96))

    return ' '.join(alpha_list)

print(alphabet_position("The sunset sets at twelve o' clock."))
print("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")