import random
import re
import itertools

def roll(n, x):
    result = 0
    for i in range(1, n + 1):
        result += random.randrange(1, x + 1)
    return result

def roll_expression(expression):
    result = 0
    expression = expression.replace(" ", "")
    pieces = re.findall('\+?-?\d*d?\d+', expression)
    for piece in itertools.chain(pieces):
        die = False
        if re.match('.*d', piece):
            die = True
            n, x = re.findall('\d+', piece)
            n, x = int(n), int(x)
        if re.match('-', piece):
            if die: result -= roll(n, x)
            else: result += int(piece)
        else:
            if die: result += roll(n, x)
            else: result += int(piece)
    return result
