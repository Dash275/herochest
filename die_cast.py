import random

def cast(stcast):
    '''Expected input: String with valid die roll expression (?x[d]y+?z)'''
    stcast = stcast.replace(" ", "")
    for letter in stcast:
        lscast = stcast.split("+")
    for i in lscast:
        if i == "+":
            del lscast[i]
    total = 0
    for die in lscast:
        roll = 0
        lsdie = die.split("d")
        if len(lsdie) == 2:
            if lsdie[0] == "":
                lsdie[0] = 1
            while lsdie[0]:
                roll += random.randrange(1, int(lsdie[1]) + 1)
                lsdie[0] = int(lsdie[0]) - 1
        else:
            total += int(die)
        total += roll
    return total

def die(y = 20, x = 1):
    roll = 0
    while x:
        roll += random.randrange(1, y + 1)
        x += -1
    return roll
