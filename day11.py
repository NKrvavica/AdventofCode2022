# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 09:37:15 2022

@author: Nino
"""

from aoc import *
from collections import deque, defaultdict
import math
import copy


def parse_input(notes):
    monkey_dict = {}
    for n, monkey in enumerate(notes):
        temp = {}
        rules = monkey.split('\n')
        items = deque(integers(rules[1]))
        temp['items'] = items
        _, operation = rules[2].split(' = ')
        func = eval(f'lambda old: {operation}')
        temp['func'] = func
        temp['divider'] = integers(rules[3])[0]
        temp['if_True'] = integers(rules[4])[0]
        temp['if_False'] = integers(rules[5])[0]
        temp['inspected'] = 0
        monkey_dict[n] = temp
    return monkey_dict


def inspection(part, monkey_dict, N, lcm=None):
    for r in range(N):
        for monkey in monkey_dict:

            this_monkey = monkey_dict[monkey]

            while this_monkey['items']:
                item = this_monkey['items'].popleft()
                monkey_dict[monkey]['inspected'] += 1
                level = this_monkey['func'](item)

                if part == 1:
                    level = math.floor(level / 3) # part 1
                else:
                    level = level % lcm # part 2

                if level % this_monkey['divider'] == 0:
                    to_monkey = this_monkey['if_True']
                else:
                    to_monkey = this_monkey['if_False']

                monkey_dict[to_monkey]['items'].append(level)

    inspected = [monkey_dict[monkey]['inspected'] for monkey in monkey_dict]

    inspected.sort()
    monkey_business = inspected[-2] * inspected[-1]
    return monkey_business



notes = read_input('day11', sep='\n\n')
monkey_dict = parse_input(notes)

# part 1
monkey_business1 = inspection(1, copy.deepcopy(monkey_dict), 20)
print(monkey_business1)


# part 2
dividers = [monkey_dict[monkey]['divider'] for monkey in monkey_dict]
lcm = math.prod(dividers)
monkey_business2 = inspection(2, monkey_dict, 10_000, lcm)
print(monkey_business2)
