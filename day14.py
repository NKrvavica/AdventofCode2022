# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:38:30 2022

@author: Nino
"""
from aoc import *
import numpy as np
import matplotlib.pyplot as plt

structures = read_input('day14')

rocks = []
for struc in structures:
    points = struc.split(' -> ')
    for a, b in zip(points[:-1], points[1:]):
        x1, y1 = integers(a)
        x2, y2 = integers(b)
        if x1 == x2:
            ys = list(range(min(y1, y2), max(y1, y2)+1))
            xs = [x1] * len(ys)
        else:
            xs = list(range(min(x1, x2), max(x1, x2)+1))
            ys = [y1] * len(xs)
        rocks += [(x, y) for x, y in zip(xs, ys)]

#find horizon
horizon = max([y for x, y in rocks]) + 2

# part 1
filled = set(rocks)
source = 500, 0
stop = False
while not stop:
    x, y = source
    can_move = True
    while can_move:
        if (x, y + 1) not in filled:
            y += 1
        elif (x - 1, y + 1) not in filled:
            y += 1
            x -= 1
        elif (x + 1, y + 1) not in filled:
            y += 1
            x += 1
        else:
            can_move = False
            filled.add((x, y))
        if y > horizon:
            stop = True
            break

part1 = len(filled.difference(set(rocks)))
print(part1)

# plot part 1
miny = 0
maxy = horizon
minx = min([x for x, y in rocks]) + 1
maxx = max([x for x, y in rocks]) + 1
dx = maxx - minx + 2
cave = np.zeros((maxy, dx))
for x, y in list(filled):
    cave[y, x - minx + 1] = 1
for x, y in rocks:
    cave[y, x - minx + 1] = 2
plt.imshow(cave)



# part 2
bottom = horizon
filled = set(rocks)
source = 500, 0
stop = False
while not stop:
    if source in filled:
        break
    x, y = source
    can_move = True
    while can_move:
        if (x, y + 1) not in filled and y < bottom-1:
            y += 1
        elif (x - 1, y + 1) not in filled and y < bottom-1:
            y += 1
            x -= 1
        elif (x + 1, y + 1) not in filled and y < bottom-1:
            y += 1
            x += 1
        else:
            can_move = False
            filled.add((x, y))

part2 = len(filled.difference(set(rocks)))
print(part2)
