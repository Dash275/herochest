import die_cast as dc

def initiative(character):
    '''Expected input: Object with initiative instance var.'''
    roll = dc.die()
    roll += character.initiative
    return roll
