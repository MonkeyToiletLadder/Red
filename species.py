'''
    species.py
    Dylan Wisswell Vaxeral
    Igloo version 0.1.0
    March 10 2020
    Description: Pokemon generation one clone.
'''

from typing import List, Dict
from pokety import Type
from stats import Stats
from moves import moves
from growth import Growth
from evolution import Evolution

class Species:
    
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
        evolutions: List[Evolution]
    ):
        self.name = name
        self.pokedex_number = pokedex_number
        self.base_stats = base_stats
        self.primary_type = primary_type
        self.secondary_type = secondary_type
        self.catch_rate = catch_rate
        self.base_experience_yield = base_experience_yield
        self.starting_moves = starting_moves
        self.machine_moves = machine_moves
        self.learned_moves = learned_moves
        self.growth = growth
        self.evolutions = evolutions

BULBASAUR = 1
IVYSAUR = 2
VENUSAUR = 3
CHARMANDER = 4
CHARMELEON = 5
CHARIZARD = 6
SQUIRTLE = 7
WARTORTLE = 8
BLASTOISE = 9
CATERPIE = 10
METAPOD = 11
BUTTERFREE = 12
WEEDLE = 13
KAKUNA = 14
BEEDRILL = 15
PIDGEY = 16
PIDGEOTTO = 17
PIDGEOT = 18
RATTATA = 19
RATICATE = 20
SPEAROW = 21
FEAROW = 22
EKANS = 23
ARBOK = 24
PIKACHU = 25
RAICHU = 26
SANDSHREW = 27
SANDSLASH = 28
NIDORAN_F = 29
NIDORINA = 30
NIDOQUEEN = 31
NIDORAN_M = 32
NIDORINO = 33
NIDOKING = 34
CLEFAIRY = 35
CLEFABLE = 36
VULPIX = 37
NINTALES = 38
JIGGLYPUFF = 39
WIGGLYTUFF = 40
ZUBAT = 41
GOLBAT = 42
ODDISH = 43
GLOOM = 44
VILEPLUME = 45
PARAS = 46
PARASECT = 47
VENONAT = 48
VENOMOTH = 49
DIGLETT = 50
DUGTRIO = 51
MEOWTH = 52
PERSIAN = 53
PSYDUCK = 54
GOLDUCK = 55
MANKEY = 56
PRIMEAPE = 57
GROWLITHE = 58
ARCANINE = 59
POLIWAG = 60
POLIWHIRL = 61
POLIWRATH = 62
ABRA = 63
KADABRA = 64
ALAKAZAM = 65
MACHOP = 66
MACHOKE = 67
MACHAMP = 68
BELLSPROUT = 69
WEEPINBELL = 70
VICTREEBEL = 71
TENTACOOL = 72
TENTACRUEL = 73
GEODUDE = 74
GRAVELER = 75
GOLEM = 76
PONYTA = 77
RAPIDASH = 78
SLOWPOKE = 79
SLOWBRO = 80
MAGNEMITE = 81
MAGNETON = 82
FARFETCHD = 83
DODUO = 84
DODRIO = 85
SEEL = 86
DEWGONG = 87
GRIMER = 88
MUK = 89
SHELLDER = 90
CLOYSTER = 91
GASTLY = 92
HAUNTER = 93
GENGAR = 94
ONIX = 95
DROWZEE = 96
HYPNO = 97
KRABBY = 98
KINGLER = 99
VOLTORB = 100
ELECTRODE = 101
EXEGGCUTE = 102
EXEGGUTOR = 103
CUBONE = 104
MAROWAK = 105
HITMONLEE = 106
HITMONCHAN = 107
LICKITUNG = 108
KOFFING = 109
WEEZING = 110
RHYHORN = 111
RHYDON = 112
CHANSEY = 113
TANGELA = 114
KANGASKHAN = 115
HORSEA = 116
SEADRA = 117
GOLDEEN = 118
SEAKING = 119
STARYU = 120
STARMIE = 121
MR_MIME = 122
SCYTHER = 123
JYNX = 124
ELECTABUZZ = 125
MAGMAR = 126
PINSIR = 127
TAUROS = 128
MAGIKARP = 129
GYARADOS = 130
LAPRAS = 131
DITTO = 132
EEVEE = 133
VAPOREON = 134
JOLTEON = 135
FLAREON = 136
PORYGON = 137
OMANYTE = 138
OMASTAR = 139
KABUTO = 140
KABUTOPS = 141
AERODACTYL = 142
SNORLAX = 143
ARTICUNO = 144
ZAPADOS = 145
MOLTRES = 146
DRATINI = 147
DRAGONAIR = 148
DRAGONITE = 149
MEWTWO = 150
MEW = 151

species = [
    
    Species(# 153
        "Bulbasaur",
        BULBASAUR,
        Stats(45,49,49,45,65),
        Type.Grass,
        Type.Poison,
        45,
        64,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(IVYSAUR, level=16)
        ]
    ),

    Species(# 9
        "Ivysaur",
        IVYSAUR,
        Stats(60,62,63,60,80),
        Type.Grass,
        Type.Poison,
        45,
        141,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(VENUSAUR, level=32)
        ]
    ),

    Species(# 154
        "Venusaur",
        VENUSAUR,
        Stats(80,82,83,80,100),
        Type.Grass,
        Type.Poison,
        45,
        208,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 176
        "Charmander",
        CHARMANDER,
        Stats(39,52,43,65,50),
        Type.Fire,
        Type.Empty,
        45,
        65,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(CHARMELEON, level=16)
        ]
    ),

    Species(# 178
        "Charmeleon",
        CHARMELEON,
        Stats(58,64,58,80,65),
        Type.Fire,
        Type.Empty,
        45,
        142,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(CHARIZARD, level=36)
        ]
    ),

    Species(# 180
        "Charizard",
        6,
        Stats(78,84,78,100,85),
        Type.Fire,
        Type.Flying,
        45,
        209,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 177
        "Squirtle",
        SQUIRTLE,
        Stats(44,48,65,43,50),
        Type.Water,
        Type.Empty,
        45,
        66,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(WARTORTLE, level=16)
        ]
    ),

    Species(# 179
        "Wartortle",
        WARTORTLE,
        Stats(59,63,80,58,65),
        Type.Water,
        Type.Empty,
        45,
        143,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(BLASTOISE, level=36)
        ]
    ),

    Species(# 28
        "Blastoise",
        BLASTOISE,
        Stats(79,83,100,78,85),
        Type.Water,
        Type.Empty,
        45,
        210,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 123
        "Caterpie",
        CATERPIE,
        Stats(45,30,35,45,20),
        Type.Bug,
        Type.Empty,
        255,
        53,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(METAPOD, level=7)
        ]
    ),

    Species(# 124
        "Metapod",
        METAPOD,
        Stats(50,20,55,30,25),
        Type.Bug,
        Type.Empty,
        120,
        72,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(BUTTERFREE, level=10)
        ]
    ),

    Species(# 125
        "Butterfree",
        BUTTERFREE,
        Stats(60,45,50,70,80),
        Type.Bug,
        Type.Flying,
        45,
        160,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 112
        "Weedle",
        WEEDLE,
        Stats(40,35,30,50,20),
        Type.Bug,
        Type.Poison,
        255,
        52,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(KAKUNA, level=7)
        ]
    ),

    Species(# 113
        "Kakuna",
        KAKUNA,
        Stats(45,25,50,35,25),
        Type.Bug,
        Type.Poison,
        120,
        71,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(BEEDRILL, level=10)
        ]
    ),

    Species(# 114
        "Beedrill",
        BEEDRILL,
        Stats(65,80,40,75,45),
        Type.Bug,
        Type.Poison,
        45,
        159,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 36
        "Pidgey",
        PIDGEY,
        Stats(40,45,40,56,35),
        Type.Normal,
        Type.Flying,
        255,
        55,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(PIDGEOTTO, level=18)
        ]
    ),

    Species(# 150
        "Pidgeotto",
        PIDGEOTTO,
        Stats(63,60,55,71,50),
        Type.Normal,
        Type.Flying,
        120,
        113,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(PIDGEOT, level=36)
        ]
    ),

    Species(# 151
        "Pidgeot",
        PIDGEOT,
        Stats(83,80,75,91,70),
        Type.Normal,
        Type.Flying,
        45,
        172,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 165
        "Rattata",
        RATTATA,
        Stats(30,56,35,72,25),
        Type.Normal,
        Type.Empty,
        255,
        57,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(RATICATE, level=20)
        ]
    ),

    Species(# 166
        "Raticate",
        RATICATE,
        Stats(55,81,60,97,50),
        Type.Normal,
        Type.Empty,
        127,
        116,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 5
        "Spearow",
        SPEAROW,
        Stats(40,60,30,70,31),
        Type.Normal,
        Type.Flying,
        225,
        58,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(FEAROW, level=20)
        ]
    ),

    Species(# 35
        "Fearow",
        FEAROW,
        Stats(65,90,65,100,61),
        Type.Normal,
        Type.Flying,
        90,
        162,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 108
        "Ekans",
        EKANS,
        Stats(35,60,44,55,40),
        Type.Poison,
        Type.Empty,
        225,
        62,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(ARBOK, level=22)
        ]
    ),

    Species(# 45
        "Arbok",
        ARBOK,
        Stats(60,85,69,80,65),
        Type.Poison,
        Type.Empty,
        90,
        147,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 84
        "Pikachu",
        PIKACHU,
        Stats(35,55,30,90,50),
        Type.Electric,
        Type.Empty,
        190,
        82,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(RAICHU, item="thunder_stone")
        ]
    ),

    Species(# 85
        "Raichu",
        RAICHU,
        Stats(60,90,55,100,90),
        Type.Electric,
        Type.Empty,
        75,
        122,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 96
        "Sandshrew",
        SANDSHREW,
        Stats(50,75,85,40,30),
        Type.Ground,
        Type.Empty,
        255,
        93,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(SANDSLASH, level=22)
        ]
    ),

    Species(# 97
        "Sandslash",
        SANDSLASH,
        Stats(75,100,110,65,55),
        Type.Ground,
        Type.Empty,
        90,
        163,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 15
        "Nidoran♀",
        NIDORAN_F,
        Stats(55,47,52,41,40),
        Type.Poison,
        Type.Empty,
        235,
        59,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(NIDORINA, level=16)
        ]
    ),

    Species(# 168
        "Nidorina",
        NIDORINA,
        Stats(70,62,67,56,55),
        Type.Poison,
        Type.Empty,
        120,
        117,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(NIDOQUEEN, item="moon_stone")
        ]
    ),

    Species(# 16
        "Nidoqueen",
        NIDOQUEEN,
        Stats(90,82,87,76,75),
        Type.Poison,
        Type.Ground,
        45,
        194,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 3
        "Nidoran♂",
        NIDORAN_M,
        Stats(46,57,40,50,40),
        Type.Poison,
        Type.Empty,
        235,
        60,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(NIDORINO, level=16)
        ]
    ),

    Species(# 167
        "Nidorino",
        NIDORINO,
        Stats(61,72,57,65,55),
        Type.Poison,
        Type.Empty,
        120,
        118,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(NIDOKING, item="moon_stone")
        ]
    ),

    Species(# 7
        "Nidoking",
        NIDOKING,
        Stats(81,92,77,85,75),
        Type.Poison,
        Type.Ground,
        45,
        195,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 4
        "Clefairy",
        CLEFAIRY,
        Stats(70,45,48,35,60),
        Type.Normal,
        Type.Empty,
        150,
        68,
        [],
        [],
        {},
        Growth.Fast,
        [
            Evolution(CLEFABLE, item="moon_stone")
        ]
    ),

    Species(# 142
        "Clefable",
        CLEFABLE,
        Stats(95,70,73,60,85),
        Type.Normal,
        Type.Empty,
        25,
        129,
        [],
        [],
        {},
        Growth.Fast,
        []
    ),

    Species(# 82
        "Vulpix",
        VULPIX,
        Stats(38,41,40,65,65),
        Type.Fire,
        Type.Empty,
        190,
        63,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(NINTALES, item="fire_stone")
        ]
    ),

    Species(# 83
        "Ninetales",
        NINTALES,
        Stats(73,76,75,100,100),
        Type.Fire,
        Type.Empty,
        75,
        178,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 100
        "Jigglypuff",
        JIGGLYPUFF,
        Stats(115,45,20,20,25),
        Type.Normal,
        Type.Empty,
        170,
        76,
        [],
        [],
        {},
        Growth.Fast,
        [
            Evolution(WIGGLYTUFF, item="moon_stone")
        ]
    ),

    Species(# 101
        "Wigglytuff",
        WIGGLYTUFF,
        Stats(140,70,45,45,50),
        Type.Normal,
        Type.Empty,
        50,
        109,
        [],
        [],
        {},
        Growth.Fast,
        []
    ),

    Species(# 107
        "Zubat",
        ZUBAT,
        Stats(40,45,35,55,40),
        Type.Poison,
        Type.Flying,
        225,
        54,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(GOLBAT, level=22)
        ]
    ),

    Species(# 130
        "Golbat",
        GOLBAT,
        Stats(75,80,70,90,75),
        Type.Poison,
        Type.Flying,
        90,
        171,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 185
        "Oddish",
        ODDISH,
        Stats(45,50,55,30,75),
        Type.Grass,
        Type.Poison,
        255,
        78,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(GLOOM, level=21)
        ]
    ),

    Species(# 186
        "Gloom",
        GLOOM,
        Stats(60,65,70,40,85),
        Type.Grass,
        Type.Poison,
        120,
        132,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(VILEPLUME, item="leaf_stone")
        ]
    ),

    Species(# 187
        "Vileplume",
        VILEPLUME,
        Stats(75,80,85,50,100),
        Type.Grass,
        Type.Poison,
        45,
        184,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 109
        "Paras",
        PARAS,
        Stats(35,70,55,25,55),
        Type.Bug,
        Type.Grass,
        190,
        70,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(PARASECT, level=24)
        ]
    ),

    Species(# 46
        "Parasect",
        PARASECT,
        Stats(60,95,80,30,80),
        Type.Bug,
        Type.Grass,
        75,
        128,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 65
        "Venonat",
        VENONAT,
        Stats(60,55,50,45,40),
        Type.Bug,
        Type.Poison,
        190,
        75,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(VENOMOTH, level=31)
        ]
    ),

    Species(# 119
        "Venomoth",
        VENOMOTH,
        Stats(70,65,60,90,90),
        Type.Bug,
        Type.Poison,
        75,
        138,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 59
        "Diglett",
        DIGLETT,
        Stats(10,55,25,95,45),
        Type.Ground,
        Type.Empty,
        225,
        81,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(DUGTRIO, level=26)
        ]
    ),

    Species(# 118
        "Dugtrio",
        DUGTRIO,
        Stats(35,80,50,120,70),
        Type.Ground,
        Type.Empty,
        50,
        153,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 77
        "Meowth",
        MEOWTH,
        Stats(40,45,35,90,40),
        Type.Normal,
        Type.Empty,
        255,
        69,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(PERSIAN, level=28)
        ]
    ),

    Species(# 144
        "Persian",
        PERSIAN,
        Stats(65,70,60,115,65),
        Type.Normal,
        Type.Empty,
        90,
        148,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 47
        "Psyduck",
        PSYDUCK,
        Stats(50,52,48,55,50),
        Type.Water,
        Type.Empty,
        190,
        80,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(GOLDUCK, level=33)
        ]
    ),

    Species(# 128
        "Golduck",
        GOLDUCK,
        Stats(80,82,78,85,80),
        Type.Water,
        Type.Empty,
        75,
        174,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 57
        "Mankey",
        MANKEY,
        Stats(40,80,35,70,35),
        Type.Fighting,
        Type.Empty,
        190,
        74,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(PRIMEAPE, level=28)
        ]
    ),

    Species(# 117
        "Primeape",
        PRIMEAPE,
        Stats(65,105,60,95,60),
        Type.Fighting,
        Type.Empty,
        75,
        149,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 33
        "Growlithe",
        GROWLITHE,
        Stats(55,70,45,60,50),
        Type.Fire,
        Type.Empty,
        190,
        91,
        [],
        [],
        {},
        Growth.Slow,
        [
            Evolution(ARCANINE, item="fire_stone")
        ]
    ),

    Species(# 20
        "Arcanine",
        ARCANINE,
        Stats(90,110,80,95,80),
        Type.Fire,
        Type.Empty,
        75,
        213,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 71
        "Poliwag",
        POLIWAG,
        Stats(40,50,40,90,40),
        Type.Water,
        Type.Empty,
        255,
        77,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(POLIWHIRL, level=25)
        ]
    ),

    Species(# 110
        "Poliwhirl",
        POLIWHIRL,
        Stats(65,65,65,90,50),
        Type.Water,
        Type.Empty,
        120,
        131,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(POLIWRATH, item="water_stone")
        ]
    ),

    Species(# 111
        "Poliwrath",
        POLIWRATH,
        Stats(90,85,95,70,70),
        Type.Water,
        Type.Fighting,
        45,
        185,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 148
        "Abra",
        ABRA,
        Stats(25,20,15,90,105),
        Type.Psychic,
        Type.Empty,
        200,
        73,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(KADABRA, level=16)
        ]
    ),

    Species(# 38
        "Kadabra",
        KADABRA,
        Stats(40,35,30,105,120),
        Type.Psychic,
        Type.Normal,
        100,
        145,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(ALAKAZAM, trade=True)
        ]
    ),

    Species(# 149
        "Alakazam",
        ALAKAZAM,
        Stats(55,50,45,120,135),
        Type.Psychic,
        Type.Empty,
        50,
        186,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 106
        "Machop",
        MACHOP,
        Stats(70,80,50,35,35),
        Type.Fighting,
        Type.Empty,
        180,
        88,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(MACHOKE, level=28)
        ]
    ),

    Species(# 41
        "Machoke",
        MACHOKE,
        Stats(80,100,70,45,50),
        Type.Fighting,
        Type.Empty,
        90,
        146,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(MACHAMP, trade=True)
        ]
    ),

    Species(# 126
        "Machamp",
        MACHAMP,
        Stats(90,130,80,55,65),
        Type.Fighting,
        Type.Empty,
        45,
        193,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 188
        "Bellsprout",
        BELLSPROUT,
        Stats(50,75,35,40,70),
        Type.Grass,
        Type.Poison,
        255,
        84,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(WEEPINBELL, level=21)
        ]
    ),

    Species(# 189
        "Weepinbell",
        WEEPINBELL,
        Stats(65,90,50,55,85),
        Type.Grass,
        Type.Poison,
        120,
        151,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(VICTREEBEL, item="leaf_stone")
        ]
    ),

    Species(# 190
        "Victreebel",
        VICTREEBEL,
        Stats(80,105,65,70,100),
        Type.Grass,
        Type.Poison,
        45,
        191,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 24
        "Tentacool",
        TENTACOOL,
        Stats(40,40,35,70,100),
        Type.Water,
        Type.Poison,
        190,
        105,
        [],
        [],
        {},
        Growth.Slow,
        [
            Evolution(TENTACRUEL, level=30)
        ]
    ),

    Species(# 155
        "Tentacruel",
        TENTACRUEL,
        Stats(80,70,65,100,120),
        Type.Water,
        Type.Poison,
        60,
        205,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 169
        "Geodude",
        GEODUDE,
        Stats(40,80,100,20,30),
        Type.Rock,
        Type.Ground,
        255,
        86,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(GRAVELER, level=25)
        ]
    ),

    Species(# 39
        "Graveler",
        GRAVELER,
        Stats(55,95,115,35,45),
        Type.Rock,
        Type.Ground,
        120,
        134,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(GOLEM, trade=True)
        ]
    ),

    Species(# 49
        "Golem",
        GOLEM,
        Stats(80,110,130,45,55),
        Type.Rock,
        Type.Ground,
        45,
        177,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 163
        "Ponyta",
        PONYTA,
        Stats(50,85,55,90,65),
        Type.Fire,
        Type.Empty,
        190,
        152,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(RAPIDASH, level=40)
        ]
    ),

    Species(# 164
        "Rapidash",
        RAPIDASH,
        Stats(65,100,70,105,80),
        Type.Fire,
        Type.Empty,
        60,
        192,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 37
        "Slowpoke",
        SLOWPOKE,
        Stats(90,65,65,15,40),
        Type.Water,
        Type.Psychic,
        190,
        99,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(SLOWBRO, level=37)
        ]
    ),

    Species(# 8
        "Slowbro",
        SLOWBRO,
        Stats(95,75,110,30,80),
        Type.Water,
        Type.Psychic,
        75,
        164,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 173
        "Magnemite",
        MAGNEMITE,
        Stats(25,35,70,45,95),
        Type.Electric,
        Type.Empty,
        190,
        89,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(MAGNETON, level=30)
        ]
    ),

    Species(# 54
        "Magnetom",
        MAGNETON,
        Stats(50,60,95,70,120),
        Type.Electric,
        Type.Empty,
        60,
        161,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 64
        "Farhetch'd",
        FARFETCHD,
        Stats(52,65,55,60,58),
        Type.Normal,
        Type.Flying,
        45,
        94,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 70
        "Doduo",
        DODUO,
        Stats(35,85,45,75,35),
        Type.Normal,
        Type.Flying,
        190,
        96,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(DODRIO, level=31)
        ]
    ),

    Species(# 116
        "Dodrio",
        DODRIO,
        Stats(60,110,70,100,60),
        Type.Normal,
        Type.Flying,
        45,
        158,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 58
        "Seel",
        SEEL,
        Stats(65,45,55,45,70),
        Type.Water,
        Type.Empty,
        190,
        100,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(DEWGONG, level=34)
        ]
    ),

    Species(# 120
        "Dewgong",
        DEWGONG,
        Stats(90,70,80,70,95),
        Type.Water,
        Type.Ice,
        75,
        176,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 13
        "Grimer",
        GRIMER,
        Stats(80,80,50,25,40),
        Type.Poison,
        Type.Empty,
        190,
        90,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(MUK, level=38)
        ]
    ),

    Species(# 136
        "Muk",
        MUK,
        Stats(105,105,75,50,65),
        Type.Poison,
        Type.Empty,
        75,
        157,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 23
        "Shellder",
        SHELLDER,
        Stats(30,65,100,40,45),
        Type.Water,
        Type.Empty,
        190,
        97,
        [],
        [],
        {},
        Growth.Slow,
        [
            Evolution(CLOYSTER, item="water_stone")
        ]
    ),

    Species(# 139
        "Cloyster",
        CLOYSTER,
        Stats(50,95,180,70,85),
        Type.Water,
        Type.Ice,
        60,
        203,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 25
        "Gastly",
        GASTLY,
        Stats(30,35,30,80,100),
        Type.Ghost,
        Type.Poison,
        190,
        95,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(HAUNTER, level=25)
        ]
    ),

    Species(# 147
        "Haunter",
        HAUNTER,
        Stats(45,50,45,95,115),
        Type.Ghost,
        Type.Poison,
        90,
        126,
        [],
        [],
        {},
        Growth.MediumSlow,
        [
            Evolution(GENGAR, trade=True)
        ]
    ),

    Species(# 14
        "Gengar",
        GENGAR,
        Stats(60,65,60,110,130),
        Type.Ghost,
        Type.Poison,
        45,
        190,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    ),

    Species(# 34
        "Onix",
        ONIX,
        Stats(35,45,160,70,30),
        Type.Rock,
        Type.Ground,
        45,
        108,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 48
        "Drowzee",
        DROWZEE,
        Stats(60,48,45,42,90),
        Type.Psychic,
        Type.Empty,
        190,
        102,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(HYPNO, level=26)
        ]
    ),

    Species(# 129
        "Hypno",
        HYPNO,
        Stats(85,73,70,67,115),
        Type.Psychic,
        Type.Empty,
        75,
        165,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 78
        "Krabby",
        KRABBY,
        Stats(30,105,90,50,25),
        Type.Water,
        Type.Normal,
        255,
        115,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(KINGLER, level=28)
        ]
    ),

    Species(# 138
        "Kingler",
        KINGLER,
        Stats(55,130,115,75,50),
        Type.Water,
        Type.Empty,
        60,
        206,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 6
        "Voltorb",
        VOLTORB,
        Stats(40,30,50,100,55),
        Type.Electric,
        Type.Empty,
        190,
        103,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(ELECTRODE, level=30)
        ]
    ),

    Species(# 141
        "Electrode",
        ELECTRODE,
        Stats(60,50,70,140,80),
        Type.Electric,
        Type.Empty,
        60,
        150,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 12
        "Exeggcute",
        EXEGGCUTE,
        Stats(60,40,80,40,60),
        Type.Grass,
        Type.Psychic,
        90,
        98,
        [],
        [],
        {},
        Growth.Slow,
        [
            Evolution(EXEGGUTOR, item="leaf_stone")
        ]
    ),

    Species(# 10
        "Exeggutor",
        EXEGGUTOR,
        Stats(95,95,85,55,125),
        Type.Grass,
        Type.Psychic,
        45,
        212,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 17
        "Cubone",
        CUBONE,
        Stats(50,50,95,35,40),
        Type.Ground,
        Type.Empty,
        190,
        87,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(MAROWAK, level=28)
        ]
    ),

    Species(# 145
        "Marowak",
        MAROWAK,
        Stats(60,80,110,45,50),
        Type.Ground,
        Type.Empty,
        75,
        124,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 43
        "Hitmonlee",
        HITMONLEE,
        Stats(50,105,79,76,35),
        Type.Fighting,
        Type.Empty,
        45,
        139,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 44
        "Hitmonchan",
        HITMONCHAN,
        Stats(50,105,79,76,35),
        Type.Fighting,
        Type.Empty,
        45,
        140,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 11
        "Lickitung",
        LICKITUNG,
        Stats(90,55,75,30,60),
        Type.Normal,
        Type.Empty,
        45,
        127,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 55
        "Koffing",
        KOFFING,
        Stats(40,65,95,35,60),
        Type.Poison,
        Type.Empty,
        190,
        114,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(WEEZING, level=35)
        ]
    ),

    Species(# 143
        "Weezing",
        WEEZING,
        Stats(65,90,120,60,85),
        Type.Poison,
        Type.Normal,
        60,
        173,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 18
        "Rhyhorn",
        RHYHORN,
        Stats(80,85,95,25,30),
        Type.Ground,
        Type.Rock,
        120,
        135,
        [],
        [],
        {},
        Growth.Slow,
        [
            Evolution(RHYDON, level=42)
        ]
    ),

    Species(# 1
        "Rhydon",
        RHYDON,
        Stats(105,130,120,40,45),
        Type.Ground,
        Type.Rock,
        60,
        204,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 40
        "Chansey",
        CHANSEY,
        Stats(250,5,5,50,105),
        Type.Normal,
        Type.Empty,
        30,
        255,
        [],
        [],
        {},
        Growth.Fast,
        []
    ),

    Species(# 30
        "Tangela",
        TANGELA,
        Stats(65,55,115,60,100),
        Type.Grass,
        Type.Grass,
        45,
        166,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 2
        "Kangaskhan",               
        KANGASKHAN,
        Stats(105,95,80,90,40),
        Type.Normal,
        Type.Empty,
        45,
        175,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 92
        "Horsea",
        HORSEA,
        Stats(30,40,70,60,70),
        Type.Water,
        Type.Empty,
        225,
        83,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(SEADRA, level=32)
        ]
    ),

    Species(# 93
        "Seadra",
        SEADRA,
        Stats(55,65,95,85,95),
        Type.Water,
        Type.Empty,
        75,
        155,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 157
        "Goldeen",
        GOLDEEN,
        Stats(45,67,60,63,50),
        Type.Water,
        Type.Empty,
        225,
        111,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(SEAKING, level=33)
        ]
    ),

    Species(# 158
        "Seaking",
        SEAKING,
        Stats(80,92,65,68,80),
        Type.Water,
        Type.Empty,
        60,
        170,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 27
        "Staryu",
        STARYU,
        Stats(30,45,55,85,70),
        Type.Water,
        Type.Empty,
        225,
        106,
        [],
        [],
        {},
        Growth.Slow,
        [
            Evolution(STARMIE, item="water_stone")
        ]
    ),

    Species(# 152
        "Starmie",
        STARMIE,
        Stats(60,75,85,115,100),
        Type.Water,
        Type.Psychic,
        60,
        207,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 42
        "Mr. Mime",
        MR_MIME,
        Stats(40,45,65,90,100),
        Type.Psychic,
        Type.Empty,
        45,
        136,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 26
        "Scyther",
        SCYTHER,
        Stats(70,110,80,105,55),
        Type.Bug,
        Type.Flying,
        45,
        187,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 72
        "Jynx",
        JYNX,
        Stats(65,50,35,95,95),
        Type.Ice,
        Type.Psychic,
        45,
        137,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 53
        "Electabuzz",
        ELECTABUZZ,
        Stats(65,83,57,105,85),
        Type.Electric,
        Type.Empty,
        45,
        156,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 51
        "Magmar",
        MAGMAR,
        Stats(65,95,57,93,85),
        Type.Fire,
        Type.Empty,
        45,
        167,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 29
        "Pinsir",
        PINSIR,
        Stats(65,125,100,85,55),
        Type.Bug,
        Type.Empty,
        45,
        200,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 60
        "Tauros",
        TAUROS,
        Stats(75,100,95,110,70),
        Type.Normal,
        Type.Empty,
        45,
        221,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 133
        "Magikarp",
        MAGIKARP,
        Stats(20,10,55,80,20),
        Type.Water,
        Type.Empty,
        255,
        20,
        [],
        [],
        {},
        Growth.Slow,
        [
            Evolution(GYARADOS, level=20)
        ]
    ),

    Species(# 22
        "Gyarados",
        GYARADOS,
        Stats(95,125,79,81,100),
        Type.Water,
        Type.Flying,
        45,
        214,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 19
        "Lapras",
        LAPRAS,
        Stats(130,85,80,60,95),
        Type.Water,
        Type.Ice,
        45,
        219,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 76
        "Ditto",
        DITTO,
        Stats(48,48,48,48,48),
        Type.Normal,
        Type.Empty,
        35,
        61,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 102
        "Eevee",
        EEVEE,
        Stats(55,55,50,55,65),
        Type.Normal,
        Type.Empty,
        45,
        92,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(VAPOREON, item="water_stone"),
            Evolution(JOLTEON, item="thunder_stone"),
            Evolution(FLAREON, item="fire_stone")
        ]
    ),

    Species(# 105
        "Vaporeon",
        VAPOREON,
        Stats(130,65,60,65,110),
        Type.Water,
        Type.Empty,
        45,
        196,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 104
        "Jolteon",
        JOLTEON,
        Stats(65,65,60,130,110),
        Type.Electric,
        Type.Empty,
        45,
        197,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 103
        "Flareon",
        FLAREON,
        Stats(65,130,60,65,110),
        Type.Fire,
        Type.Empty,
        45,
        198,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 170
        "Porygon",
        PORYGON,
        Stats(65,60,70,40,75),
        Type.Normal,
        Type.Empty,
        45,
        130,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 98
        "Omanyte",
        OMANYTE,
        Stats(35,40,100,35,90),
        Type.Rock,
        Type.Water,
        45,
        120,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(OMASTAR, level=40)
        ]
    ),

    Species(# 99
        "Omastar",
        OMASTAR,
        Stats(70,60,125,55,115),
        Type.Rock,
        Type.Water,
        45,
        199,
        [],
        [],
        {},
        Growth.MediumFast,
        []
    ),

    Species(# 91
        "Kabutops",
        KABUTOPS,
        Stats(60,115,105,80,70),
        Type.Rock,
        Type.Water,
        45,
        201,
        [],
        [],
        {},
        Growth.MediumFast,
        [
            Evolution(KABUTOPS, level=40)
        ]
    ),

    Species(# 171
        "Aerodactyl",
        AERODACTYL,
        Stats(80,105,65,130,60),
        Type.Rock,
        Type.Flying,
        45,
        202,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 132
        "Snorlax",
        SNORLAX,
        Stats(160,110,65,30,65),
        Type.Normal,
        Type.Empty,
        25,
        154,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 74
        "Articuno",
        ARTICUNO,
        Stats(90,85,100,85,125),
        Type.Ice,
        Type.Flying,
        3,
        215,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 75
        "Zapdos",
        ZAPADOS,
        Stats(90,90,85,100,125),
        Type.Electric,
        Type.Flying,
        3,
        216,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 73
        "Moltres",
        MOLTRES,
        Stats(90,100,90,90,125),
        Type.Fire,
        Type.Flying,
        3,
        217,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 88
        "Dratini",
        DRATINI,
        Stats(41,64,45,50,50),
        Type.Dragon,
        Type.Empty,
        45,
        67,
        [],
        [],
        {},
        Growth.Slow,
        [
            Evolution(DRAGONAIR, level=30)
        ]
    ),

    Species(# 89
        "Dragonair",
        DRAGONAIR,
        Stats(61,84,65,70,70),
        Type.Dragon,
        Type.Normal,
        45,
        144,
        [],
        [],
        {},
        Growth.Slow,
        [
            Evolution(DRAGONITE, level=55)
        ]
    ),

    Species(# 66
        "Dragonite",
        DRAGONITE,
        Stats(91,134,95,80,100),
        Type.Dragon,
        Type.Flying,
        45,
        218,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 131
        "Mewtwo",
        MEWTWO,
        Stats(106,110,90,130,154),
        Type.Psychic,
        Type.Empty,
        3,
        220,
        [],
        [],
        {},
        Growth.Slow,
        []
    ),

    Species(# 21
        "Mew",
        MEW,
        Stats(100,100,100,100,100),
        Type.Psychic,
        Type.Empty,
        45,
        64,
        [],
        [],
        {},
        Growth.MediumSlow,
        []
    )
]
