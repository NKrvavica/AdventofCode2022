# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:29:02 2022

@author: Nino
"""

from aoc import *
import string

contents = read_input('day03')

priority = string.ascii_lowercase + string.ascii_uppercase

part1, part2 = 0, 0
group= []
for n, c in enumerate(contents):
    c1, c2 = c[:len(c)//2], c[len(c)//2:]
    common = set(c1).intersection(set(c2)).pop()
    part1 += priority.find(common)+1
    # part 2
    group.append(set(c))
    if (n+1) % 3 == 0: # new group
        badge = group[0].intersection(group[1]).intersection(group[2]).pop()
        part2 += priority.find(badge)+1
        group = []

print(part1)

print(part2)
