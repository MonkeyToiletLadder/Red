'''
    evolution.py
    Dylan Wisswell Vaxeral
    Igloo version 0.1.0
    March 10 2020
    Description: Pokemon generation one clone.
'''

class Evolution:

    def __init__(self, pokedex_number, **keywords):
        self.species_index = pokedex_number - 1
        self.level = keywords.get('level', None)
        self.item = keywords.get('item', None)
        self.move = keywords.get('move', None)
        self.trade = keywords.get('trade', None)

    def meets_requirements(self, pokemon: 'Pokemon') -> bool:
        if self.level and pokemon.level < self.level:
            return False
        if self.item and pokemon.item != self.item:
            return False
        if self.move and not pokemon.has_move(self.move):
            return False
        # if self.trade != None and not self.trade:
        #     return False
        if self.trade ^ pokemon.by_trade:
            return False

        pokemon.by_trade = False

        return True

if True:
print("")
