# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 08:13:30 2022

@author: Nino
"""

from aoc import *
import networkx as nx
import copy


def parse_input(puzzle):
    G = nx.DiGraph()
    for line in puzzle:
        monkey, rest = line.split(': ')
        try:
            res = int(rest)
            monkey1, monkey2, ops = '', '', ''
        except:
            res = ''
            monkey1 = rest[:4]
            monkey2 = rest[7:]
            ops = rest[5]
        G.add_node(monkey, res=res,
                           op=ops,
                           a=monkey1,
                           b=monkey2)
    for node in G.nodes:
        if len(G.nodes[node]['op']) > 0:
            G.add_edge(node, G.nodes[node]['a'])
            G.add_edge(node, G.nodes[node]['b'])
    return G


def solve(G):
    progress = True
    while len(G.nodes) > 1 and progress:
        progress = False
        leafs = [x for x in G.nodes() if G.out_degree(x)==0]
        for leaf in leafs:
            if type(G.nodes[leaf]['res']) == int:
                branch = list(G.predecessors(leaf))[0]
                if G.nodes[branch]['a'] == leaf:
                    G.nodes[branch]['a'] = G.nodes[leaf]['res']
                elif G.nodes[branch]['b'] == leaf:
                    G.nodes[branch]['b'] = G.nodes[leaf]['res']
                G.remove_node(leaf)
                progress = True
            elif (type(G.nodes[leaf]['a']) == int and
                  type(G.nodes[leaf]['b']) == int):
                a, b, op = (G.nodes[leaf]['a'],
                            G.nodes[leaf]['b'],
                            G.nodes[leaf]['op'])
                G.nodes[leaf]['res'] = int(eval(f'{a} {op} {b}'))
                progress = True
    return G


# load and parse input
puzzle = read_input('day21')
G = parse_input(puzzle)
list(G.nodes(data=True))
list(G.edges(data=True))


# part 1
G1 = solve(copy.deepcopy(G))
print(G1.nodes['root']['a'] + G1.nodes['root']['b'])


# part 2
G.nodes['humn']['res'] = '?'
G2 = solve(G)
list(G2.nodes(data=True))

# identify branch where 'humn' is and set root equality!
if type(G2.nodes['root']['a']) == int:
    branch = G2.nodes['root']['b']
    G2.nodes['root']['b'] =  G2.nodes['root']['a']
    G2.nodes[branch]['res'] =  G2.nodes['root']['b']
else:
    branch = G2.nodes['root']['a']
    G2.nodes['root']['a'] =  G2.nodes['root']['b']
    G2.nodes[branch]['res'] =  G2.nodes['root']['a']

branch = 'root'
while branch != 'humn':
    res, a, b, op = (G2.nodes[branch]['res'],
                     G2.nodes[branch]['a'],
                     G2.nodes[branch]['b'],
                     G2.nodes[branch]['op'])
    if type(a) == int:                      # b is unknown
        next_branch = b
        if op == '+':
            b = res - a
        elif op == '-':
            b = a - res
        elif op == '*':
            b = int(res / a)
        else:
            b = int(a / res)
        G2.nodes[next_branch]['res'] = b
        branch = next_branch
    else:                                   # a is unknown
        next_branch = a
        if op == '+':
            a = res - b
        elif op == '-':
            a = res + b
        elif op == '*':
            a = int(res / b)
        else:
            a = int(res * b)
        G2.nodes[next_branch]['res'] = a
        branch = next_branch

print(G2.nodes['humn']['res'])
