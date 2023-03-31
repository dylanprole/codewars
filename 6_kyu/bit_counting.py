# https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def count_bits(n):
    BYTES = 8
    integer_binary = [0]*BYTES*8
    bit_values = [2**i for i in range(BYTES*8)][::-1]

    for i in range(len(integer_binary)):
        integer_binary[i] = 1
        integer_value = sum([integer_binary[i]*bit_values[i] for i in range(BYTES*8)])
        if integer_value == n:
            break
        elif integer_value > n:
            integer_binary[i] = 0

    return integer_binary.count(1)


