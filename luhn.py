__version__ = '0.1.0'

def checksum(string):
    digits = map(int, string)
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def verify(string):
    return (checksum(string) == 0)

def generate(string):
    cksum = checksum(string + '0')
    return (10 - cksum) % 10
