# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:59:25 2022

@author: Nino
"""

from aoc import *
import numpy as np

elves = read_input('day01', sep=' ')[0].split('\n\n')

max_cal = []
for group in elves:
    cal = np.array(integers(group)).sum()
    max_cal.append(cal)
cal_sorted = np.sort(np.array(max_cal))

print(cal_sorted[-1])
print(cal_sorted[-3:].sum())
