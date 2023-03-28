# https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s):
    if len(s) <= 2:
        return s
    else:
        return get_middle(s[1:-1])
