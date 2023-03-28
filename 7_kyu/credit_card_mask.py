# https://www.codewars.com/kata/5412509bd436bd33920011bc

# return masked string
def maskify(cc):
    # If string length is 4 or less
    # just return the string
    if len(cc) <= 4:
        return cc
    
    # Create mask of length of
    # string minus last 4 chars
    mask = '#'*(len(cc)-4)
    
    # Add final 4 chars of string
    masked_cc = mask + cc[-4:]
    
    # Return masked string
    return masked_cc
