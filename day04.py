# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:45:14 2022

@author: Nino
"""

from aoc import *

pairs = read_input('day04')

def get_set(string):
    lower, upper = integers(string, negative=False)
    return set(range(lower, upper+1))


part1, part2 = 0, 0

for pair in pairs:
    first, second = pair.split(',')
    set1, set2 = get_set(first), get_set(second)
    if set1.issubset(set2) or set2.issubset(set1):
        part1 += 1
    if len(set1.intersection(set2)) > 0:
        part2 += 1

print(part1)
print(part2)
