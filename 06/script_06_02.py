#!/usr/bin/python
import math
input_file = 'input.txt'

def get_parents(data, child):
    parents = []
    while 'COM' not in parents:
        parents += [orbit[0] for orbit in data if orbit[1] == child]
        child = parents[-1]
    return parents

def main():
    fp = open(input_file)
    data = [row.strip().split(')') for row in fp.readlines()]
#     data = [row.strip().split(')') for row in """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN""".split('\n')]
    you_parents = get_parents(data, 'YOU')
    san_parents = get_parents(data, 'SAN')
    print len(set(you_parents).symmetric_difference(set(san_parents)))
    fp.close()

if __name__ == "__main__":
   main()