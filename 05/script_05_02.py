#!/usr/bin/python
import math
input_file = 'input.txt'

def process_opcode(data, index, _input):
    # print 'index:', index, '_input:', _input
    if data[index] == 1:
        # print 'processing 1:', data[index : index + 4]
        data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
        index += 4
    elif data[index] == 2:
        # print 'processing 2:', data[index : index + 4]
        data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
        index += 4
    elif data[index] == 3:
        # print 'processing 3:', data[index : index + 2]
        data[data[index + 1]] = _input
        index += 2
    elif data[index] == 4:
        # print 'processing 4:', data[index : index + 2]
        _input = data[data[index + 1]]
        index += 2
    elif data[index] == 5:
        # print 'processing 5:', data[index : index + 2]
        index = data[index + 2] if data[index + 1] else index + 2
    elif data[index] == 6:
        # print 'processing 6:', data[index : index + 2]
        index = data[index + 2] if not data[index + 1] else index + 2
    elif data[index] == 7:
        # print 'processing 7:', data[index : index + 4]
        data[data[index + 3]] = data[data[index + 1]] < data[data[index + 2]]
        index += 4
    elif data[index] == 8:
        # print 'processing 8:', data[index : index + 4]
        data[data[index + 3]] = data[data[index + 1]] == data[data[index + 2]]
        index += 4
    elif data[index] == 99:
        print _input
        return
    else:
        # print 'processing x:', data[index : index + 4]
        e = data[index] / 1 % 10
        d = data[index] / 10 % 10
        c = data[index] / 100 % 10
        b = data[index] / 1000 % 10
        a = data[index] / 10000 % 10
        de = d * 10 + e
        # print a, b, c, d, e, '(', de, ')'
        if de == 1:
            result = int(data[index + 1] if c else data[data[index + 1]]) + int(data[index + 2] if b else data[data[index + 2]])
            if a:
                data[index + 3] = result
            else:
                data[data[index + 3]] = result
            index += 4
        elif de == 2:
            result = int(data[index + 1] if c else data[data[index + 1]]) * int(data[index + 2] if b else data[data[index + 2]])
            if a:
                data[index + 3] = result
            else:
                data[data[index + 3]] = result
            index += 4
        elif de == 3:
            if c:
                data[index + 1] = _input
            else:
                data[data[index + 1]]
            index += 2
        elif de == 4:
            _input = int(data[index + 1] if c else data[data[index + 1]])
            index += 2
        elif de == 5:
            index = int(data[index + 2] if b else data[data[index + 2]]) if int(data[index + 1] if c else data[data[index + 1]]) else index + 3
        elif de == 6:
            index = int(data[index + 2] if b else data[data[index + 2]]) if not int(data[index + 1] if c else data[data[index + 1]]) else index + 3
        elif de == 7:
            result = int(data[index + 1] if c else data[data[index + 1]]) < int(data[index + 2] if b else data[data[index + 2]])
            data[data[index + 3]] = result
            index += 4
        elif de == 8:
            result = int(data[index + 1] if c else data[data[index + 1]]) == int(data[index + 2] if b else data[data[index + 2]])
            data[data[index + 3]] = result
            index += 4
        else:
            # print 'de unknown:', de
            return
    # print data
    process_opcode(data, index, _input)

def main():
    fp = open(input_file)
    data = [int(i) for i in fp.read().split(',')]

    # data = [int(i) for i in '3,9,8,9,10,9,4,9,99,-1,8'.split(',')]
    # process_opcode(data, 0, 8) # True if == 0
    # data = [int(i) for i in '3,9,7,9,10,9,4,9,99,-1,8'.split(',')]
    # process_opcode(data, 0, 7) # True if < 8
    # data = [int(i) for i in '3,3,1108,-1,8,3,4,3,99'.split(',')]
    # process_opcode(data, 0, 7) # True if == 8
    # data = [int(i) for i in '3,3,1107,-1,8,3,4,3,99'.split(',')]
    # process_opcode(data, 0, 8) # True if < 8
    
    # data = [int(i) for i in '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'.split(',')]
    # process_opcode(data, 0, 9) # 999 if < 8; 1000 if == 8; 1001 if > 8

    process_opcode(data, 0, 5)
    fp.close()

if __name__ == "__main__":
   main()