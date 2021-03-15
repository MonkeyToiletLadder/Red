'''
    species.py
    Dylan Wisswell Vaxeral
    Igloo version 0.1.0
    March 10 2020
    Description: Pokemon generation one clone.
'''

from typing import *
from type import *
from stats import *
from moves import *
from growth import *
from evolution import *

class Species:
    name: str
    pokedex_number: int
    base_stats: Stats
    primary_type: Type
    secondary_type: Type
    catch_rate: int
    base_experience_yield: int
    starting_moves: List[int]
    machine_moves: List[int]
    learned_moves: Dict[int, int]
    growth_rate: Growth
    evolution: Evolution

    def __init__(
        self,
        name: str,
        pokedex_number: int,
        base_stats: Stats,
        primary_type: Type,
        secondary_type: Type,
        catch_rate: int,
        base_experience_yield: int,
        starting_moves: List[int],
        machine_moves: List[int],
        learned_moves: Dict[int, int],
        growth: Growth,
        evolution: Evolution
    ):
        self.name = name
        self.pokedex_number = pokedex_number
        self.base_stats = base_stats
        self.primary_type = primary_type
        self.secondary_type = secondary_type
        self.catch_rate = catch_rate
        base_experience_yield = base_experience_yield
        self.starting_moves = starting_moves
        self.machine_moves = machine_moves
        self.learned_moves = learned_moves
        self.growth = growth
        self.evolution = evolution

species = [
    Species(# 1
        "Rhydon",                   # Name
        112,                        # Pokedex Number
        Stats(105,130,120,40,45),   # Stats HP, ATTACK, DEFENSE, SPEED, SPECIAL
        Type.Ground,                # Primary Type
        Type.Rock,                  # Secondary Type
        60,                         # Catch Rate
        204,                        # Base Experience Yield
        [],                         # Starting Moves
        [],                         # Machine Moves
        {},                         # Learned Moves
        Growth.Slow,                # Growth
        None                        # Evolution
    ),
    Species(# 2
        "Kangaskhan",               
        115,
        Stats(105,95,80,90,40),
        Type.Normal,
        Type.Empty,
        45,
        175,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 3
        "Nidoran♂",
        32,
        Stats(46,57,40,50,40),
        Type.Poison,
        Type.Empty,
        235,
        60,
        [],
        [],
        {},
        Growth.MediumSlow,
        Evolution()
    ),
    Species(# 4
        "Clefairy",
        35,
        Stats(70,45,48,35,60),
        Type.Normal,
        Type.Empty,
        150,
        68,
        [],
        [],
        {},
        Growth.Fast,
        None
    ),
    Species(# 5
        "Spearow",
        21,
        Stats(40,60,30,70,31),
        Type.Normal,
        Type.Flying,
        225,
        58,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 6
        "Voltorb",
        100,
        Stats(40,30,50,100,55),
        Type.Electric,
        Type.Empty,
        190,
        103,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 7
        "Nidoking",
        34,
        Stats(81,92,77,85,75),
        Type.Poison,
        Type.Ground,
        45,
        195,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 8
        "Slowbro",
        80,
        Stats(95,75,110,30,80),
        Type.Water,
        Type.Psychic,
        75,
        164,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 9
        "Ivysaur",
        2,
        Stats(60,62,63,60,80),
        Type.Grass,
        Type.Poison,
        45,
        141,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 10
        "Exeggutor",
        103,
        Stats(95,95,85,55,125),
        Type.Grass,
        Type.Psychic,
        45,
        212,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 11
        "Lickitung",
        108,
        Stats(90,55,75,30,60),
        Type.Normal,
        Type.Empty,
        45,
        127,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 12
        "Exeggcute",
        102,
        Stats(60,40,80,40,60),
        Type.Grass,
        Type.Psychic,
        90,
        98,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 13
        "Grimer",
        88,
        Stats(80,80,50,25,40),
        Type.Poison,
        Type.Empty,
        190,
        90,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 14
        "Gengar",
        94,
        Stats(60,65,60,110,130),
        Type.Ghost,
        Type.Poison,
        45,
        190,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 15
        "Nidoran♀",
        29,
        Stats(55,47,52,41,40),
        Type.Poison,
        Type.Empty,
        235,
        59,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 16
        "Nidoqueen",
        31,
        Stats(90,82,87,76,75),
        Type.Poison,
        Type.Ground,
        45,
        194,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 17
        "Cubone",
        104,
        Stats(50,50,95,35,40),
        Type.Ground,
        Type.Empty,
        190,
        87,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 18
        "Rhyhorn",
        111,
        Stats(80,85,95,25,30),
        Type.Ground,
        Type.Rock,
        120,
        135,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 19
        "Lapras",
        131,
        Stats(130,85,80,60,95),
        Type.Water,
        Type.Ice,
        45,
        219,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 20
        "Arcanine",
        59,
        Stats(90,110,80,95,80),
        Type.Fire,
        Type.Empty,
        75,
        213,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 21
        "Mew",
        151,
        Stats(100,100,100,100,100),
        Type.Psychic,
        Type.Empty,
        45,
        64,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 22
        "Gyarados",
        130,
        Stats(95,125,79,81,100),
        Type.Water,
        Type.Flying,
        45,
        214,
        [],
        [],
        {},
        Growth.Slow
    ),
    Species(# 23
        "Shellder",
        90,
        Stats(30,65,100,40,45),
        Type.Water,
        Type.Empty,
        190,
        97,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 24
        "Tentacool",
        72,
        Stats(40,40,35,70,100),
        Type.Water,
        Type.Poison,
        190,
        105,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 25
        "Gastly",
        92,
        Stats(30,35,30,80,100),
        Type.Ghost,
        Type.Poison,
        190,
        95,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 26
        "Scyther",
        123,
        Stats(70,110,80,105,55),
        Type.Bug,
        Type.Flying,
        45,
        187,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 27
        "Staryu",
        120,
        Stats(30,45,55,85,70),
        Type.Water,
        Type.Empty,
        225,
        106,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 28
        "Blastoise",
        9,
        Stats(79,83,100,78,85),
        Type.Water,
        Type.Empty,
        45,
        210,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 29
        "Pinsir",
        127,
        Stats(65,125,100,85,55),
        Type.Bug,
        Type.Empty,
        45,
        200,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 30
        "Tangela",
        114,
        Stats(65,55,115,60,100),
        Type.Grass,
        Type.Grass,
        45,
        166,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 31
        "MissingNo.",
        0,
        Stats(33,136,0,29,6),
        Type.Bird,
        Type.Normal,
        29,
        143,
        [],
        [],
        {},
        Growth.Fast,
        None
    ),
    Species(# 32
        "MissingNo.",
        0,
        Stats(33,136,0,29,6),
        Type.Bird,
        Type.Normal,
        29,
        143,
        [],
        [],
        {},
        Growth.Fast,
        None
    ),
    Species(# 33
        "Growlithe",
        58,
        Stats(55,70,45,60,50),
        Type.Fire,
        Type.Empty,
        190,
        91,
        [],
        [],
        {},
        Growth.Slow,
        None
    ),
    Species(# 34
        "Onix",
        95,
        Stats(35,45,160,70,30),
        Type.Rock,
        Type.Ground,
        45,
        108,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 35
        "Fearow",
        22,
        Stats(65,90,65,100,61),
        Type.Normal,
        Type.Flying,
        90,
        162,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 36
        "Pidgey",
        16,
        Stats(40,45,40,56,35),
        Type.Normal,
        Type.Flying,
        255,
        55,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 37
        "Slowpoke",
        79,
        Stats(90,65,65,15,40),
        Type.Water,
        Type.Psychic,
        190,
        99,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(# 38
        "Kadabra",
        64,
        Stats(40,35,30,105,120),
        Type.Psychic,
        Type.Normal,
        100,
        145,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 39
        "Graveler",
        75,
        Stats(55,95,115,35,45),
        Type.Rock,
        Type.Ground,
        120,
        134,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 40
        "Chansey",
        113,
        Stats(250,5,5,50,105),
        Type.Normal,
        Type.Empty,
        30,
        255,
        [],
        [],
        {},
        Growth.Fast,
        None
    ),
    Species(# 41
        "Machoke",
        67,
        Stats(80,100,70,45,50),
        Type.Fighting,
        Type.Empty,
        90,
        146,
        [],
        [],
        {},
        Growth.MediumSlow,
        None
    ),
    Species(# 42
        "Mr. Mime",
        122,
        Stats(40,45,65,90,100),
        Type.Psychic,
        Type.Empty,
        45,
        136,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    ),
    Species(
        "Hitmonlee",
        106,
        Stats(50,105,79,76,35),
        Type.Fighting,
        Type.Empty,
        45,
        139,
        [],
        [],
        {},
        Growth.MediumFast,
        None
    )
]
