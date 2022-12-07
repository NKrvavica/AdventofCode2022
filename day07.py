# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:33:48 2022

@author: Nino
"""

from aoc import *
import networkx as nx
import matplotlib.pyplot as plt


commands = read_input('day07')

G = nx.DiGraph()

# root node
node_id, cwd_id, cwd_name = 1, 1, '/'
G.add_node(node_id, name=cwd_name, size=0, ftype=0)

for c in commands[1:]:
    if c[:4] == '$ cd':        # go to folder
        _, _, folder_name = c.split(' ')
        if folder_name == '..': # one step back
            cwd_id = list(G.predecessors(cwd_id))[0]
        else: # one step forward
            for n in list(G.successors(cwd_id)):
                if G.nodes[n]['name']==folder_name:
                    cwd_id = n
                    break
        cwd_name = G.nodes[cwd_id]['name']
        print(c, f' -> goto to folder {cwd_name} ({cwd_id})')
    elif c[:4] == '$ ls':
        continue
    elif c[:3] == 'dir': # add folder node
        _, fname = c.split(' ')
        node_id += 1
        print(c, f' -> add folder {fname} ({node_id}) to folder {cwd_name} ({cwd_id})')
        G.add_node(node_id, name=fname, size=0, ftype=0)
        G.add_edge(cwd_id, node_id)
    else: # add file node
        size, file = c.split(' ')
        node_id += 1
        print(c, f' -> add file {file} ({node_id}) to folder {cwd_name} ({cwd_id})')
        G.add_node(node_id, name=file, size = int(size), ftype=1)
        G.add_edge(cwd_id, node_id)


# part 1
part1 = 0
for node in nx.nodes(G):
    for n in nx.descendants(G, node):
        G.nodes[node]['size'] += G.nodes[n]['size']
    if G.nodes[node]['ftype'] == 0 and G.nodes[node]['size'] <= 100_000:
        part1 += G.nodes[node]['size']

print(part1)


# part 2
free_space = 70_000_000 - G.nodes[1]['size']
needed_space = 30_000_000 - free_space

space = 1e9
for node in nx.nodes(G):
    if  (G.nodes[node]['ftype'] == 0 and
         space > G.nodes[node]['size'] >= needed_space):
        space = G.nodes[node]['size']

print(space)
