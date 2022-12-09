# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 08:31:13 2022

@author: Nino
"""

from aoc import *
import numpy as np

motions = read_input('day09')

directions = {'R': np.array([0, 1]), 'L': np.array([0, -1]),
              'U': np.array([-1, 0]), 'D': np.array([1, 0])}


def move_rope(N, motions):
    knots = np.zeros((N, 2))
    visited = set()
    visited.add(knots[-1, 0] + knots[-1, 1]*1j)
    for motion in motions:
        direc, step = motion.split(' ')
        for _ in range(int(step)):
            knots[0, :] += directions[direc]
            for rope in range(1, len(knots)):
                dist = knots[rope-1, :] - knots[rope, :]
                if (abs(dist) > 1).any():
                    knots[rope, :] += np.array([sign(dist[0]), sign(dist[1])])
                if rope == N-1:
                    visited.add(knots[rope, 0] + knots[rope, 1]*1j)
    return len(visited)


# part 1
print(move_rope(2, motions))

# part 2
print(move_rope(10, motions))
