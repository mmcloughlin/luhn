__version__ = '0.2.0'

def checksum(string):
    """
    Compute the Luhn checksum for the provided string of digits. Note this
    assumes the check digit is in place.
    """
    digits = list(map(int, string))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def verify(info):
    """
    Check if the provided string of digits satisfies the Luhn checksum.

    >>> verify('356938035643809')
    True
    >>> verify('534618613411236')
    False
    """
    if type(info) == int:
        info = str(info)
    return (checksum(info) == 0)

def generate(info):
    """
    Generate the Luhn check digit to append to the provided string.

    >>> generate('35693803564380')
    9
    >>> generate('53461861341123')
    4
    """
    if type(info) == int:
        info = str(info)
    cksum = checksum(info + '0')
    return (10 - cksum) % 10

def append(info):
    """
    Append Luhn check digit to the end of the provided string.

    >>> append('53461861341123')
    '534618613411234'
    """
    if type(info) == int:
        info = str(info)    
    return info + str(generate(info))
