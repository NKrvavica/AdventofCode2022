# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 08:29:00 2022

@author: Nino
"""

# signal = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
# signal = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
# signal = 'nppdvjthqldpwncqszvftbrmjlhg'
# signal = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
# signal = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'


from aoc import *


def how_many_chars(N):
    for i in range(len(signal)):
        if len(set(signal[i:i+N])) == N:
            print(i+N)
            return i+N


signal = read_input('day06')[0]

part1 = how_many_chars(4)

part2 = how_many_chars(14)
