# https://www.codewars.com/kata/55fd2d567d94ac3bc9000064

def row_sum_odd_numbers(n):
    return sum([i for i in range((n**2 - n + 1), (n**2 + n), 2)])