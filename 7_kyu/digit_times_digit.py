# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    return int(''.join([str(int(dig)**2) for dig in str(num)]))
