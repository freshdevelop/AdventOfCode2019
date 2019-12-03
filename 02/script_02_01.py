#!/usr/bin/python
import math
input_file = 'input.txt'

def process_opcode(data, index):
    print 'processing', data[index:index + 4]
    if data[index] == 1:
        data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
    elif data[index] == 2:
        data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
    elif data[index] == 99:
        print 'finish', data[0]
        return
    print data
    process_opcode(data, index + 4)

def main():
    fp = open(input_file)
    data = [int(i) for i in fp.read().split(',')]
    data[1] = 12
    data[2] = 2
    # data = [int(i) for i in '1,9,10,3,2,3,11,0,99,30,40,50'.split(',')]
    process_opcode(data, 0)
    print(data)
    fp.close()

if __name__ == "__main__":
   main()