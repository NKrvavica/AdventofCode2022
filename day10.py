# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 09:31:19 2022

@author: Nino
"""

from aoc import *
import numpy as np
import matplotlib.pyplot as plt


def add_strength(cycle, sum_strength):
    if cycle % 20 == 0:
        signal_strength = cycle * X
        if cycle in CYCLES:
            sum_strength += signal_strength
    return sum_strength


def draw_pixel(cycle, crt, X):
    position = cycle % 40
    if X <= position < X + 3:
        crt[cycle-1] = 1
    else:
        crt[cycle-1] = 0
    return crt


program = read_input('day10')

# part 1
CYCLES = [20, 60, 100, 140, 180, 220]
X, cycle, sum_strength = 1, 0, 0
for ins in program:
    if ins == 'noop':
        cycle += 1
        sum_strength = add_strength(cycle, sum_strength)
    else: # addx
        command, value = ins.split(' ')
        for i in range(2):
            cycle += 1
            sum_strength = add_strength(cycle, sum_strength)
        X += int(value)

print(sum_strength)


# part 2
X, cycle = 1, 0
crt = np.zeros(240)
for ins in program:
    if ins == 'noop':
        cycle += 1
        crt = draw_pixel(cycle, crt, X)
    else: # addx
        command, value = ins.split(' ')
        for i in range(2):
            cycle += 1
            crt = draw_pixel(cycle, crt, X)
        X += int(value)

crt_show = crt.reshape(6, 40)
print(crt_show)
plt.imshow(crt_show)
