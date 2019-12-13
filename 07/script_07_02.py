#!/usr/bin/python
# coding: utf-8
from itertools import permutations
input_file = 'input.txt'

def process_opcode(amps, amp, _input):

    while True:
        data, _phase, index, phase_setting = amps[amp]

        # print 'caso:', data[index], phase_setting
        # print 'in  > amp:', amp, 'index:', index, '_input:', _input, 'data:', data
        if data[index] == 1:
            # print 'processing 1:', data[index : index + 4]
            # print data[data[index + 1]] + data[data[index + 2]], 'in position', data[index + 3], '( was', data[data[index + 3]], ')'
            data[data[index + 3]] = data[data[index + 1]] + data[data[index + 2]]
            index += 4
        elif data[index] == 2:
            # print 'processing 2:', data[index : index + 4]
            data[data[index + 3]] = data[data[index + 1]] * data[data[index + 2]]
            index += 4
        elif data[index] == 3:
            # print 'processing 3:', data[index : index + 2]
            # print _phase if phase_setting else _input, 'in position', data[index + 1], '( was', data[data[index + 1]], ')'
            data[data[index + 1]] = _phase if phase_setting else _input
            index += 2
        elif data[index] == 4:
            # print 'processing 4:', data[index : index + 2]
            _input = data[data[index + 1]]
            index += 2
            # print 'switch amp [2]:', amp, _input
            # print 'out > amp:', amp, 'index:', index, '_input:', _input, 'data:', data
            amps[amp] = data, _phase, index, False
            amp = (amp + 1) % len(amps)
            continue
            # index = 0
            # return
            # process_opcode(amps, (amp + 1) % len(amps), 0, _input)
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
            # print _input
            # print 'amp:', amp
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
                # print result, '(', int(data[index + 1] if c else data[data[index + 1]]), '+', int(data[index + 2] if b else data[data[index + 2]]), ') in position', target, '( was', data[target], ')'
                data[target] = result
                index += 4
            elif de == 2:
                result = int(data[index + 1] if c else data[data[index + 1]]) * int(data[index + 2] if b else data[data[index + 2]])
                target = index + 3 if a else data[index + 3]
                # print result, 'in position', target, '( was', data[target], ')'
                data[target] = result
                index += 4
            elif de == 3:
                target = index + 1 if c else data[index + 1]
                data[target] = result
                index += 2
            elif de == 4:
                _input = int(data[index + 1] if c else data[data[index + 1]])
                index += 2
                # print 'switch amp [2]:', amp, _input
                # print 'out > amp:', amp, 'index:', index, '_input:', _input, 'data:', data
                # print '-' * 20
                amps[amp] = data, _phase, index, False
                amp = (amp + 1) % len(amps)
                continue
                # index = 0
                # return
                # process_opcode(amps, (amp + 1) % len(amps), 0, _input)
            elif de == 5:
                index = int(data[index + 2] if b else data[data[index + 2]]) if int(data[index + 1] if c else data[data[index + 1]]) else index + 3
                # print 'skipping index to', index
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

        # process_opcode(amps, amp, index, _input)
        amps[amp] = data, _phase, index, False
        # print 'out > amp:', amp, 'index:', index, '_input:', _input, 'data:', data
        # print '-' * 5
        # return

def process_phases(data, phases):
    amps = [[data[:], phase, 0, True] for phase in phases]  # data, starting phase, index, phase_setting (flag)
    return process_opcode(amps, 0, 0)                       # amps data
                                                            # current amp (ad ogni recursione di process_opcode() current amp = (current amp + 1) % len(amps)
                                                            # input/output value

                                                            # Hint --> https://www.reddit.com/r/adventofcode/comments/e7aqcb/2019_day_7_part_2_confused_with_the_question/
                                                            # ACHTUNG: la lista va passata come copia (data[:]) perché altrimenti ogni volta che modifico una lista si modificano tutte

def main():
    fp = open(input_file)
    data = [int(i) for i in fp.read().split(',')]

    # data = [int(i) for i in '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'.split(',')] # 139629729
    # data = [int(i) for i in '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'.split(',')] # 18216
    maximum = 0
    for phases in permutations((5, 6, 7, 8, 9)):
        maximum = max(maximum, process_phases(data, phases))

    print maximum

    fp.close()

if __name__ == "__main__":
   main()