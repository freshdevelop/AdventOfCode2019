#!/usr/bin/python
import math
input_file = 'input.txt'

def get_satellites(data, planets, distance, total):
    satellites = [row[1] for row in data if row[0] in planets]
    if satellites:
        distance += 1
        total += distance * len(satellites)
        # print satellites, distance, total
        get_satellites(data, satellites, distance, total)
    else:
        print total

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
# K)L""".split('\n')]
    get_satellites(data, ['COM'], 0, 0)
    fp.close()

if __name__ == "__main__":
   main()