# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 08:19:23 2022

@author: Nino
"""

from aoc import *
from itertools import product


puzzle = read_input('day15')


pairs = {}
beacons = set()
for pair in puzzle:
    x1, y1, x2, y2 = integers(pair)
    beacons.add((x2, y2))
    d = manhattan((x1, y1), (x2, y2))
    pairs[(x1, y1)] = ((x2, y2), d)


# part 1

row = 2_000_000

no_beacons = set()
for sensor in pairs:
    d = pairs[sensor][1]
    xs, ys = sensor
    dist_to_row = abs(row - ys)
    if dist_to_row < abs(d): # row is in sensor range
        dx = d - dist_to_row
        no_beacons.update(set(range(xs - dx, xs + dx+1)))

y_beacons = set(xs for xs, ys in beacons if ys == row)
no_beacons = no_beacons.difference(y_beacons)

print(len(no_beacons))


# part 2

def merge_intervals(intervals):
    intervals.sort()
    stack = []
    stack.append(intervals[0])
    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    return stack

N = 4_000_000

for row in range(N, 0, -1):
    # print(row)
    no_beacons = []
    for sensor in pairs:
        d = pairs[sensor][1]
        xs, ys = sensor
        dist_to_row = abs(row - ys)
        if dist_to_row < abs(d): # row is in sensor range
            dx = d - dist_to_row
            no_beacons.append([xs - dx, xs + dx+1])
    merged_intervals = merge_intervals(no_beacons)
    if len(merged_intervals) > 1:
        print(f'solution: {merged_intervals[0][1]*4_000_000+row}')
        break
