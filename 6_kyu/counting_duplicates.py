# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(text):
    return sum([1 for c in "".join(set(text.lower())) if text.lower().count(c) > 1])