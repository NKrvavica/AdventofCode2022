# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:48:26 2022

@author: Nino
"""

from aoc import *
import copy


def read_parse_input(fname):
    # read input
    with open(f"inputs/{fname}.txt") as f:
        stacks, instructions = f.read().split('\n\n')

    stcs = [list(st[1::4]) for st in stacks.split('\n')]

    # rotate list of lists
    stack_list = []
    for row in zip(*reversed(stcs[:-1])):
        stack_list.append(list(filter(lambda x: x != ' ', list(row))))

    instructions = instructions.split('\n')

    return instructions, stack_list


def stackem(instructions, stacks, part=1):
    for instruc in instructions:
        nr, s1, s2 = integers(instruc)
        if part == 1:
            stacks[s2-1] =  stacks[s2-1] + stacks[s1-1][-nr:][::-1]
        else:
            stacks[s2-1] =  stacks[s2-1] + stacks[s1-1][-nr:]
        stacks[s1-1] =  stacks[s1-1][:-nr]

    solution = ''.join(stack.pop() for stack in stacks)
    print(solution)


fname = 'day05'

instructions, stacks = read_parse_input(fname)

stacks_orig = copy.deepcopy(stacks)
stackem(instructions, stacks, part=1)
stackem(instructions, stacks_orig, part=2)
