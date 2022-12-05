# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:48:26 2022

@author: Nino
"""

from aoc import *
import pandas as pd
from collections import deque
import copy


def read_parse_input(fname):
    # read input
    puzzle = read_input(fname)

    # find empty row
    idx_empty = [i for i,x in enumerate(puzzle) if not x][0]

    # find number of stacks
    nr_stacks = integers(puzzle[idx_empty-1])[-1]

    # get instruction part
    instructions = puzzle[idx_empty+1:]

    # get stacks
    stacks_df = pd.read_fwf(f'./inputs/{fname}.txt', header=None,
                         widths=[4]*nr_stacks, nrows=idx_empty-1)
    stacks_df[stacks_df.isnull()] = ''
    stacks_df = stacks_df.iloc[::-1, :]

    # sort stacks into deque container
    stacks = []
    for n, stack in stacks_df.iteritems():
        temp = [ch[1] for ch in stack if ch != '']
        stacks.append(deque(temp))

    return instructions, stacks


fname = 'day05'

instructions, stacks = read_parse_input(fname)

stacks_orig = copy.deepcopy(stacks)

# part 1
for instruc in instructions:
    nr, s1, s2 = integers(instruc)
    for n in range(nr):
        element = stacks[s1-1].pop()
        stacks[s2-1].append(element)

part1 = ''.join(stack.pop() for stack in stacks)
print(part1)


# part 2
stacks = stacks_orig
for instruc in instructions:
    nr, s1, s2 = integers(instruc)
    buffer = ''
    for n in range(nr):
        element = stacks[s1-1].pop()
        buffer += element
    stacks[s2-1].extend(buffer[::-1])

part2 = ''.join(stack.pop() for stack in stacks)
print(part2)
