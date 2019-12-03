#!/usr/bin/python
import math
input_file = 'input.txt'

def calculate_fuel(mass):
    mass = int(mass)
    output = 0
    print 'pre', mass
    while mass > 0:
        mass = max(0, math.floor(mass / 3) - 2)
        print 'calculate', mass
        output = output + mass
    return output

def main():
    fp = open(input_file)
    print sum([calculate_fuel(i) for i in open(input_file)])
    fp.close()

    # print calculate_fuel(14)
    # print calculate_fuel(1969)

if __name__ == "__main__":
   main()