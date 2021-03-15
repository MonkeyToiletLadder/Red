'''
    evolutions.py
    Dylan Wisswell Vaxeral
    Igloo version 0.1.0
    March 10 2020
    Description: Pokemon generation one clone.
'''
from pokemon import *

class Evolution:
    species_index: int
    level: int
    item: int
    move: int

    def __init__(self, species_index, **keywords):
        self.species_index = species_index
        self.level = keywords.get('level', None)
        self.item = keywords.get('item', None)
        self.move = keywords.get('move', None)

    def meets_requirements(pokemon: Pokemon) -> bool:
        if self.level and pokemon.level < self.level:
            return False
        if self.item and pokemon.item != self.item:
            return False
        if self.move and not pokemon.has_move(self.move):
            return False
        return True
            
