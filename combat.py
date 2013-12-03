import die_cast as dc

def initiative(character):
    '''Expected input: Object with initiative instance var.'''
    roll = dc.roll(1, 20)
    roll += character.initiative
    return roll
