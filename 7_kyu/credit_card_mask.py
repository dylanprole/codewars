# DESCRIPTION:
# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

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
