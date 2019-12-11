#!/usr/bin/python
from itertools import permutations
input_file = 'input.txt'

def process_opcode(data, _phase, _input):
    index = 0
    phase_setting = True
    while True:
        # print 'index:', index, '_input:', _input, 'data:', data
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
            data[data[index + 1]] = _phase if phase_setting else _input
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
            return _input
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
                target = index + 3 if a else data[index + 3]
                data[target] = result
                index += 4
            elif de == 2:
                result = int(data[index + 1] if c else data[data[index + 1]]) * int(data[index + 2] if b else data[data[index + 2]])
                target = index + 3 if a else data[index + 3]
                # print 'result:', result, 'target:', target
                data[target] = result
                index += 4
            elif de == 3:
                target = index + 1 if c else data[index + 1]
                data[target] = result
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
                return None
        # print data
        phase_setting = False # il phase setting si applica solo al primo giro, poi si spegne. 
                              # ATTENZIONE: l'attributo data deve cominciare con 3
                              # Hint --> https://www.reddit.com/r/adventofcode/comments/e7bkj7/2019_day_7_what_is_the_meaninguse_of_the_phase/f9z5lc4/

def process_phases(data, phases):
    output = 0
    for phase in phases:
        output = process_opcode(data, phase, output)
        # break
    return output

def main():
    fp = open(input_file)
    data = [int(i) for i in fp.read().split(',')]
    # print process_opcode(data, 0)

    # data = [int(i) for i in '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'.split(',')] # 43210
    # data = [int(i) for i in '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'.split(',')] # 54321
    # data = [int(i) for i in '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'.split(',')] # 65210
    maximum = (0, 0)
    for phases in list(permutations(range(5))):
        current = (process_phases(data, phases), phases)
        maximum = current if current[0] > maximum[0] else maximum
    print maximum[0]
    
    # data = [int(i) for i in '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'.split(',')]
    # process_phases(data, [0,1,2,3,4])

    fp.close()

if __name__ == "__main__":
   main()