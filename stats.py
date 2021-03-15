'''
    stats.py
    Dylan Wisswell Vaxeral
    Igloo version 0.1.0
    March 13 2020
    Description: Pokemon generation one clone.
'''

import random

class BaseStats:
    hp: int
    attack: int
    defense: int
    speed: int
    special: int

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __iter__(self):
        return iter(self.__dict__.items())

class EffortValues(BaseStats):
    def __init__(self):
        self.hp = 0
        self.attack = 0
        self.defense = 0
        self.speed = 0
        self.special = 0

class IndividualValues(BaseStats):
    def __init__(self):
        self.attack = random.randint(0, 15)
        self.defense = random.randint(0, 15)
        self.speed = random.randint(0, 15)
        self.special = random.randint(0, 15)
        self.hp = ((1 & self.attack) << 3) | ((1 & self.defense) << 2) | ((1 & self.speed) << 1) | (1 & self.special)

class Stats(BaseStats):
    def __init__(
        self,
        hp: int,
        attack: int,
        defense: int,
        speed: int,
        special: int
    ):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.special = special
