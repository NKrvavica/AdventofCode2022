# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:14:28 2022

@author: Nino
"""

from aoc import *

pairs = read_input('day02')

points = {'X': 1, 'Y': 2, 'Z':3}
win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
draw = {'A': 'X', 'B': 'Y', 'C': 'Z'}
lose = {'A': 'Z', 'B': 'X', 'C': 'Y'}

part1 = 0
for pair in pairs:
    elf = pair[0]
    you = pair[2]
    if you == win[elf]:
        score = 6
    elif you == draw[elf]:
        score = 3
    else:
        score = 0
    print(score, points[you])
    part1 += score + points[you]

print(part1)

part2 = 0
for pair in pairs:
    elf = pair[0]
    outcome = pair[2]
    if outcome == 'X': # lose
        you = lose[elf]
        score = 0
    elif outcome == 'Y': # draw
        you = draw[elf]
        score = 3
    else:
        you = win[elf]
        score = 6
    print(score, points[you])
    part2 += score + points[you]

print(part2)
