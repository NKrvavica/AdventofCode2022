# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 08:51:56 2022

@author: Nino
"""

from aoc import *
import numpy as np


trees = read_input('day08')
array = np.array([mapl(int, line) for line in trees])


# part 1
visible_mask = np.ones_like(array)
for i in range(1, array.shape[0]-1):
    for j in range(1, array.shape[1]-1):
        if array[i, j] <= min(array[i, :j].max(),
                              array[i, j+1:].max(),
                              array[:i, j].max(),
                              array[i+1:, j].max()):
            visible_mask[i, j] = 0

print(visible_mask.sum())


# part 2
def score_view(view, height):
    view_len = np.where(view >= height)[0]
    if view_len.size == 0:
        return len(view)
    else:
        return view_len[0] + 1


score = np.zeros_like(array)
for i in range(1, array.shape[0]-1):
    for j in range(1, array.shape[1]-1):
        height = array[i, j]
        left = array[i, :j][::-1]
        right = array[i, j+1:]
        up = array[:i, j][::-1]
        down = array[i+1:, j]
        score[i, j] = (score_view(left, height)
                       * score_view(right, height)
                       * score_view(up, height)
                       * score_view(down, height))

print(score.max())
