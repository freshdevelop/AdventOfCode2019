#!/usr/bin/python
import math
input_file = 'input.txt'

def calculate_fuel(mass):
    return math.floor(int(mass) / 3) - 2

def main():
    fp = open(input_file)
    print sum([calculate_fuel(i) for i in open(input_file)])
    fp.close()

if __name__ == "__main__":
   main()