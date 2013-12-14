import random

class Hero:
    def __init__(self):
        name = ""
        self.initiative = 0
        self.strength = random.randrange(3, 19)
        self.intelligence = random.randrange(3, 19)
        self.wisdom = random.randrange(3, 19)
        self.constitution = random.randrange(3, 19)
        self.dexterity = random.randrange(3, 19)
        self.charisma = random.randrange(3, 19)
        self.update_bonuses()

    def __str__(self):
        return name

    def update_bonuses(self):
        self.str_bonus = -5 + (self.strength // 2)
        self.int_bonus = -5 + (self.intelligence // 2)
        self.wis_bonus = -5 + (self.wisdom // 2)
        self.con_bonus = -5 + (self.constitution // 2)
        self.dex_bonus = -5 + (self.dexterity // 2)
        self.cha_bonus = -5 + (self.charisma // 2)

    def name(n):
        '''If an argument, name is argument, else return name.'''
        if n and isinstance(n, str):
            self.name = n
        else:
            return name

    def initiative(n):
        '''If an argument, initiative is argument, else return initiative.'''
        if n and isinstance(n, int):
            self.initiative = n
        else:
            return self.initiative
