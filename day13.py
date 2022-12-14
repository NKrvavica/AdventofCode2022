# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 20:00:16 2022

@author: Nino
"""

from aoc import *
import copy

pairs = read_input('day13', sep='\n\n')


def compare(left, right):
    # print(left, right)
    i = 0
    while True:
        # print(i)
        # check length
        if len(left) <= i and len(right) > i:
            return True
        elif len(left) > i and len(right) <= i:
            return False
        elif len(left) <= i and len(right) <= i:
            return 9
        # get i-th values
        l = left[i]
        r = right[i]
        if type(l) == list and type(r) == list:
            # rekurzija
            res = compare(l, r)
            if res == 9:
                i += 1
            else:
                return res
        elif type(l) == int and type(r) == list:
            left[i] = [l]
        elif type(l) == list and type(r) == int:
            right[i] = [r]
        elif type(l) == int and type(r) == int:
            if l < r:
                return True
            elif l > r:
                return False
            else:
                i += 1

# part 1
ordered = []
for n, pair in enumerate(pairs):
    left, right = pair.split('\n')
    left = eval(left)
    right = eval(right)
    order = compare(left, right)
    print(f'Pair {n} -> {order}')
    if order:
        ordered.append(n+1)

print(sum(ordered))


def swap(arr, a, b):
    """ swap elements a and b in an array """
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    # return arr


def bubble_sort(unsorted, n):
    """ bubble sort algorithm """
    # iterate over unsorted array up until second last element
    for i in range(0, n - 1):
        # swapped conditions monitors for finalised list
        swapped = False
        # iterate over remaining unsorted items
        for j in range(0, n - 1 - i):
            # compare adjacent elements
            if compare(copy.deepcopy(unsorted[j+1]),
                       copy.deepcopy(unsorted[j])):
                # swap elements
                swap(unsorted, j, j + 1)
                swapped = True
        # no swaps have occured so terminate
        if not swapped:
            break
    return unsorted



# part 2
packets = []
for n, pair in enumerate(pairs):
    left, right = pair.split('\n')
    left = eval(left)
    right = eval(right)
    packets.append(left)
    packets.append(right)
two, six = [[2]], [[6]]
packets += [two, six]

sortd = bubble_sort(packets, len(packets))
print((sortd.index(two)+1)*(sortd.index(six)+1))

