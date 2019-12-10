#!/usr/bin/python
import math
input_file = 'input.txt'

def process_opcode(data, index, _input):
    # print 'index:', index, '_input:', _input
    if data[index] == 1:
        index_increase = 4
        # print 'processing 1:', data[index : index + index_increase]
        data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
    elif data[index] == 2:
        index_increase = 4
        # print 'processing 2:', data[index : index + index_increase]
        data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
    elif data[index] == 3:
        index_increase = 2
        # print 'processing 3:', data[index : index + index_increase]
        data[data[index + 1]] = _input
    elif data[index] == 4:
        index_increase = 2
        # print 'processing 4:', data[index : index + index_increase]
        _input = data[data[index + 1]]
    elif data[index] == 99:
        print _input
        return
    else:
        index_increase = 4
        # print 'processing x:', data[index : index + index_increase]
        e = data[index] / 1 % 10
        d = data[index] / 10 % 10
        c = data[index] / 100 % 10
        b = data[index] / 1000 % 10
        a = data[index] / 10000 % 10
        de = d * 10 + e
        # print a, b, c, d, e, '(', de, ')'
        if de == 1: # add
            result = int(data[index + 1] if c else data[data[index + 1]]) + int(data[index + 2] if b else data[data[index + 2]])
            if a:
                data[index + 3] = result
            else:
                data[data[index + 3]] = result
        elif de == 2: # multiply
            result = int(data[index + 1] if c else data[data[index + 1]]) * int(data[index + 2] if b else data[data[index + 2]])
            if a:
                data[index + 3] = result
            else:
                data[data[index + 3]] = result
    # print data
    # return
    process_opcode(data, index + index_increase, _input)

def main():
    fp = open(input_file)
    data = [int(i) for i in fp.read().split(',')]
    # data[1] = 12
    # data[2] = 2

    # data = [int(i) for i in '1002,4,3,4,33'.split(',')]
    # data = [int(i) for i in '3,0,4,0,99'.split(',')]
    # data = [int(i) for i in '1101,100,-1,4,0'.split(',')]
    process_opcode(data, 0, 1)
    fp.close()

if __name__ == "__main__":
   main()