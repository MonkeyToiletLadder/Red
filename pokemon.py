'''
    main.py
    Dylan Wisswell Vaxeral
    Igloo version 0.1.0
    March 10 2020
    Description: Pokemon generation one clone.
'''

from typing import List
from pokety import Type, TypeChart
from stats import Stats, IndividualValues, EffortValues
from species import *
from moves import Move
from conditions import Condition
from growth import experience_for_level
import math

type_chart = TypeChart()
print(type_chart.multiplier(Type.Fire, [Type.Water, Type.Empty]))

class Pokemon:

    def __init__(
        self,
        pokedex_number: int,
        current_hp: int,
        level: int,
        condition: Condition,
        item: int,
    ):
        assert 0 <= pokedex_number < len(species)
        assert 0 < level <= 100
        
        self.species_index = pokedex_number - 1
        self.level = level
        self.condition = condition
        self.stats = Stats(0,0,0,0,0)
        self.individual_values = IndividualValues()
        self.effort_values = EffortValues()
        self.calculate_stats()
        self.current_hp = min(current_hp, self.stats.hp)
        self.primary_type = species[self.species_index].primary_type
        self.secondary_type = species[self.species_index].secondary_type
        self.item = item
        self.moves: List[Move] = []
        self.original_trainer_id = None
        self.experience = experience_for_level(species[self.species_index].growth, self.level)
        self.by_trade = False
        
    def calculate_stats(self):
        base = self.base_stats()
        ivs = self.individual_values
        evs = self.effort_values
        for key, _ in self.stats:
            if key == 'hp':
                self.stats[key] = math.floor( ( ( ( base.hp + ivs.hp ) * 2 + math.floor( math.ceil( math.sqrt( evs.hp ) ) / 4 ) ) * self.level ) / 100 ) + self.level + 10
            else:
                self.stats[key] = math.floor( ( ( ( base[key] + ivs[key] ) * 2 + math.floor( math.ceil( math.sqrt( evs[key] ) ) / 4 ) ) * self.level ) / 100 ) + 5

    def try_evolving(self):
        evolutions = self.evolutions()
        for evolution in evolutions:
            if evolution.meets_requirements(self):
                self.species_index = evolution.species_index
                self.calculate_stats()
                break

    def has_move(self, move_index: int):
        for move in self.moves:
            if move.id == move_index:
                return True
        return False

    def species(self):
        return species[self.species_index]

    def evolutions(self):
        return species[self.species_index].evolutions

    def base_stats(self):
        return species[self.species_index].base_stats
    
p = Pokemon(HAUNTER,0,17,Condition(),0)
print(p.individual_values.__dict__)
print(p.stats.__dict__)
p.try_evolving()
print(p.stats.__dict__)
