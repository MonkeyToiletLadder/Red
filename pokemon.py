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
from species import species
from moves import Move
from conditions import Condition
from growth import experience_for_level
import math

type_chart = TypeChart()
print(type_chart.multiplier(Type.Fire, [Type.Water, Type.Empty]))

class Pokemon:
    species_index: int
    current_hp: int
    level: int
    condition: Condition
    primary_type: Type
    secondary_type: Type
    item: int
    moves: List[Move]
    original_trainer_id: int
    experience: int
    effort_values: EffortValues
    individual_values: IndividualValues
    stats: Stats
    by_trade: bool

    def __init__(
        self,
        species_index: int,
        current_hp: int,
        level: int,
        condition: Condition,
        item: int,
    ):
        assert 0 <= species_index < len(species)
        assert 0 < level <= 100
        
        self.species_index = species_index
        self.level = level
        self.condition = condition
        self.stats = Stats(0,0,0,0,0)
        self.individual_values = IndividualValues()
        self.effort_values = EffortValues()
        self.calculate_stats()
        self.current_hp = min(current_hp, self.stats.hp)
        self.primary_type = species[species_index].primary_type
        self.secondary_type = species[species_index].secondary_type
        self.item = item
        self.moves = []
        self.original_trainer_id = None
        self.experience = experience_for_level(species[species_index].growth, self.level)
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
        evolution = self.evolution()
        if evolution.meets_requirements(p):
            self.species_index = evolution.species_index
        self.calculate_stats()

    def has_move(self, move_index: int):
        for move in moves:
            if move.id == move_index:
                return True
        return False

    def species(self):
        return species[self.species_index]

    def evolution(self):
        return species[self.species_index].evolution

    def base_stats(self):
        return species[self.species_index].base_stats
    
p = Pokemon(0,0,5,Condition(),0)
print(p.stats.__dict__)
p.try_evolving()
print(p.stats.__dict__)
