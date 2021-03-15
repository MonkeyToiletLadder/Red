'''
    type.py
    Dylan Wisswell Vaxeral
    Igloo version 0.1.0
    March 10 2020
    Description: Pokemon generation one clone.
'''

from enum import Enum

class Type(Enum):
    Normal = 0
    Fire = 1
    Water = 2
    Electric = 3
    Grass = 4
    Ice = 5
    Fighting = 6
    Poison = 7
    Ground = 8
    Flying = 9
    Psychic = 10
    Bug = 11
    Rock = 12
    Ghost = 13
    Dragon = 14
    Bird = 15
    Empty = 16
    Max = 17

    def __int__(self):
        return self.value

class TypeChart:
    data = [
        #NOR:FIR:WAT:ELE:GRA:ICE:FIG:POI:GRO:FLY:PSY:BUG:ROC:GHO:DRA  <DEF
        #                                                             vATT
        [1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0.5,0  ,  1],#NOR
        [1  ,0.5,0.5,1  ,2  ,2  ,1  ,1  ,1  ,1  ,2  ,2  ,0.5,1  ,0.5],#FIR
        [0  ,2  ,0.5,1  ,0.5,1  ,1  ,1  ,2  ,1  ,1  ,1  ,2  ,1  ,0.5],#WAT
        [1  ,1  ,2  ,0.5,0.5,1  ,1  ,1  ,0  ,2  ,1  ,1  ,1  ,1  ,0.5],#ELE
        [1  ,0.5,2  ,1  ,0.5,1  ,1  ,0.5,2  ,0.5,1  ,0.5,2  ,1  ,0.5],#GRA
        [1  ,1  ,0.5,1  ,2  ,0.5,1  ,1  ,2  ,2  ,1  ,1  ,1  ,1  ,2  ],#ICE
        [2  ,1  ,1  ,1  ,1  ,2  ,1  ,0.5,1  ,0.5,0.5,0.5,2  ,0  ,1  ],#FIG
        [1  ,1  ,1  ,1  ,2  ,1  ,1  ,0.5,0.5,1  ,1  ,2  ,0.5,0.5,1  ],#POI
        [1  ,2  ,1  ,2  ,0.5,1  ,1  ,2  ,1  ,0  ,1  ,0.5,2  ,1  ,1  ],#GRO
        [1  ,1  ,1  ,0.5,2  ,1  ,2  ,1  ,1  ,1  ,1  ,2  ,0.5,1  ,1  ],#FLY
        [1  ,1  ,1  ,1  ,1  ,1  ,2  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ],#PSY
        [1  ,0.5,1  ,1  ,2  ,1  ,0.5,2  ,1  ,0.5,2  ,1  ,1  ,0.5,1  ],#BUG
        [1  ,2  ,1  ,1  ,1  ,2  ,0.5,1  ,0.5,2  ,1  ,2  ,1  ,1  ,1  ],#ROC
        [0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0  ,1  ,1  ,2  ,1  ],#GHO
        [1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,2  ],#DRA
    ]
    def __init__(self):
        pass

    def __getitem__(self, key):
        return self.data[key]

    def multiplier(self, attty, defty):
        assert len(defty) <= 2
        multiplier = 1
        for ty in defty:
            if ty == Type.Empty or ty == Type.Bird:
                continue
            multiplier *= self[int(attty)][int(ty)]
        return multiplier
