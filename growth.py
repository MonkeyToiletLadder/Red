'''
    growth.py
    Dylan Wisswell Vaxeral
    Igloo version 0.1.0
    March 10 2020
    Description: Pokemon generation one clone.
'''

import math
from enum import Enum


class Growth(Enum):
    MediumFast = 0
    MediumSlow = 1
    Fast = 2
    Slow = 3

def medium_fast(level):
    return round(level**3)

def medium_slow(level):
    return round((6 * level**3) / 5 - 15 * level**2 + 100 * level - 140)

def fast(level):
    return round((4 * level**3) / 5)

def slow(level):
    return round((5 * level**3) / 4)

def experience_for_level(growth, level):
    if growth == Growth.MediumFast:
        return medium_fast(level)
    elif growth == Growth.MediumSlow:
        return medium_slow(level)
    elif growth == Growth.Fast:
        return fast(level)
    elif growth == Growth.Slow:
        return slow(level)
