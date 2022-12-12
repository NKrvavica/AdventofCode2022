# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:48:44 2022

@author: Nino
"""

from aoc import *
import numpy as np
import collections



def find_neighbors(heightmap, current):
    neighbors = []
    for n in NEIGHBORS:
        try:
            nidx = current[0] + n[0], current[1] + n[1]
            if nidx[0] >= 0 and nidx[1] >= 0:
                if heightmap[nidx] - heightmap[current] <= 1:
                    neighbors.append(nidx)
        except:
            continue
    return neighbors


def dijkstra_search(heightmap, start_idx, end_idx):
    frontier = collections.deque()
    frontier.append((start_idx, 0))
    came_from = {start_idx: True}
    cost_so_far = {start_idx: 0}

    while len(frontier) > 0:
        current = frontier.popleft()
        # print(f"  Visiting {current}")
        if current[0] == end_idx:
            print('došao sam do kraja!')
            break
        for next in find_neighbors(heightmap, current[0]):
            new_cost = cost_so_far[current[0]] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.append((next, priority))
                came_from[next] = current
    try:
        return cost_so_far[end_idx]
    except:
        return None



NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# load and parse input
heightmap = read_input('day12')
heightmap = np.array([mapl(ord, line) for line in heightmap])

start_idx = tuple(np.argwhere(heightmap==ord('S'))[0])
heightmap[start_idx] = ord('a')
end_idx = tuple(np.argwhere(heightmap==ord('E'))[0])
heightmap[end_idx] = ord('z')


# part 1
part1 = dijkstra_search(heightmap, start_idx, end_idx)
print(part1)


# part 2
starts = np.argwhere(heightmap==ord('a'))
scores = []
for i in range(starts.shape[0]):
    start_idx = tuple(starts[i, :])
    score = dijkstra_search(heightmap, start_idx, end_idx)
    if score:
        scores.append(score)
print(min(scores))
