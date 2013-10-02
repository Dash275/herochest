import die_cast as dc

def initiative(character):
    '''Expected input: Object with initiative instance var.'''
    die[0] = "1d20"
    die[1] = str(character.initiative)
    query "".join(die, "+")
    return dc.cast(query)
