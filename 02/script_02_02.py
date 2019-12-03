#!/usr/bin/python
import math
input_file = 'input.txt'

def process_opcode(data, index, noun, verb):
    if data[index] == 1:
        data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
    elif data[index] == 2:
        data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
    elif data[index] == 99:
        if data[0] == 19690720:
            print 'result:', 100 * noun + verb
        return
    process_opcode(data, index + 4, noun, verb)

def main():
    fp = open(input_file)
    for noun in range(0, 100):
        for verb in range(0, 100):
            fp.seek(0)
            data = [int(i) for i in fp.read().split(',')]
            data[1] = noun
            data[2] = verb
            process_opcode(data, 0, noun, verb)
    fp.close()

if __name__ == "__main__":
   main()