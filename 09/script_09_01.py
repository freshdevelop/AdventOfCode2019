#!/usr/bin/python
import math
input_file = 'input.txt'

def get(data, position):
    return int(data[position]) if position < len(data) else 0

def set(data, position, value): # https://stackoverflow.com/questions/22388866/python-list-set-value-at-index-if-index-does-not-exist
    try:
        data[position] = value
    except IndexError:
        for _ in range(position - len(data) + 1):
            data.append(None)
        set(data, position, value)

def process_opcode(data, _input):
    index = 0
    base = 0
    while True:
        # print 'index:', index, 'base:', base, '_input:', _input

        if data[index] == 1:
            # print 'processing 1:', data[index : index + 4]
            set(data, get(data, index + 3), get(data, get(data, index + 1)) + get(data, get(data, index + 2)))
            index += 4
            # return
        elif data[index] == 2:
            # print 'processing 2:', data[index : index + 4]
            set(data, get(data, index + 3), get(data, get(data, index + 1)) * get(data, get(data, index + 2)))
            index += 4
            # return
        elif data[index] == 3:
            # print 'processing 3:', data[index : index + 2]
            set(data, get(data, index + 1), _input)
            index += 2
            # return
        elif data[index] == 4:
            # print 'processing 4:', data[index : index + 2]
            _input = get(data, get(data, index + 1))
            # print 'output', _input
            index += 2
            # return
        elif data[index] == 5:
            # print 'processing 5:', data[index : index + 2]
            index = get(data, index + 2) if get(data, index + 1) else index + 2
            # return
        elif data[index] == 6:
            # print 'processing 6:', data[index : index + 2]
            index = get(data, index + 2) if not get(data, index + 1) else index + 2
            # return
        elif data[index] == 7:
            # print 'processing 7:', data[index : index + 4]
            set(data, get(data, index + 3), get(data, get(data, index + 1)) < get(data, get(data, index + 2)))
            index += 4
            # return
        elif data[index] == 8:
            # print 'processing 8:', data[index : index + 4]
            set(data, get(data, index + 3), get(data, get(data, index + 1)) == get(data, get(data, index + 2)))
            index += 4
            # return
        elif data[index] == 9:
            # print 'processing 9:', data[index : index + 2]
            base += get(data, get(data, index + 1))
            index += 2
            # return
        elif data[index] == 99:
            print _input
            # print data
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
                # result = int(get(data, index + 1) if c else get(data, get(data, index + 1))) + int(get(data, index + 2) if b else get(data, get(data, index + 2)))
                if c == 0:
                    result_c = get(data, get(data, index + 1))
                elif c == 1:
                    result_c = get(data, index + 1)
                elif c == 2:
                    result_c = get(data, base + get(data, index + 1))
                if b == 0:
                    result_b = get(data, get(data, index + 2))
                elif b == 1:
                    result_b = get(data, index + 2)
                elif b == 2:
                    result_b = get(data, base + get(data, index + 2))
                result = result_c + result_b
                if a == 0:
                    set(data, get(data, index + 3), result)
                elif a == 1:
                    set(data, index + 3, result)
                elif a == 2:
                    set(data, base + get(data, index + 3), result)
                index += 4
                # return
            elif de == 2:
                # result = int(get(data, index + 1) if c else get(data, get(data, index + 1))) * int(get(data, index + 2) if b else get(data, get(data, index + 2)))
                if c == 0:
                    result_c = get(data, get(data, index + 1))
                elif c == 1:
                    result_c = get(data, index + 1)
                elif c == 2:
                    result_c = get(data, base + get(data, index + 1))
                if b == 0:
                    result_b = get(data, get(data, index + 2))
                elif b == 1:
                    result_b = get(data, index + 2)
                elif b == 2:
                    result_b = get(data, base + get(data, index + 2))
                result = result_b * result_c
                if a == 0:
                    set(data, get(data, index + 3), result)
                elif a == 1:
                    set(data, index + 3, result)
                elif a == 2:
                    set(data, base + get(data, index + 3), result)
                # print result_b, result_c, result
                # print get(data, index + 3)
                index += 4
                # print data
                # return
            elif de == 3:
                if c == 0:
                    set(data, get(data, index + 1), _input)
                elif c == 1:
                    set(data, index + 1, _input)
                elif c == 2:
                    set(data, base + get(data, index + 1), _input)
                    # print 'writing', _input, 'at position', base + get(data, index + 1)
                index += 2
                # return
            elif de == 4:
                if c == 0:
                    _input = get(data, get(data, index + 1))
                elif c == 1:
                    _input = get(data, index + 1)
                elif c == 2:
                    _input = get(data, base + get(data, index + 1))
                # print 'output', _input
                index += 2
                # return
            elif de == 5:
                # index = int(get(data, index + 2) if b else get(data, get(data, index + 2))) if int(get(data, index + 1) if c else get(data, get(data, index + 1))) else index + 3
                if c == 0:
                    result_c = get(data, get(data, index + 1))
                elif c == 1:
                    result_c = get(data, index + 1)
                elif c == 2:
                    result_c = get(data, base + get(data, index + 1))
                if result_c:
                    if b == 0:
                        index = get(data, get(data, index + 2))
                    elif b == 1:
                        index = get(data, index + 2)
                    elif b == 2:
                        index = get(data, base + get(data, index + 2))
                else:
                    index += 3
                # return
            elif de == 6:
                # index = int(get(data, index + 2) if b else get(data, get(data, index + 2))) if not int(get(data, index + 1) if c else get(data, get(data, index + 1))) else index + 3
                if c == 0:
                    result_c = get(data, get(data, index + 1))
                elif c == 1:
                    result_c = get(data, index + 1)
                elif c == 2:
                    result_c = get(data, base + get(data, index + 1))
                if not result_c:
                    if b == 0:
                        index = get(data, get(data, index + 2))
                    elif b == 1:
                        index = get(data, index + 2)
                    elif b == 2:
                        index = get(data, base + get(data, index + 2))
                else:
                    index += 3
                # return
            elif de == 7:
                # result = int(get(data, index + 1) if c else get(data, get(data, index + 1))) < int(get(data, index + 2) if b else get(data, get(data, index + 2)))
                if c == 0:
                    result_c = get(data, get(data, index + 1))
                elif c == 1:
                    result_c = get(data, index + 1)
                elif c == 2:
                    result_c = get(data, base + get(data, index + 1))
                if b == 0:
                    result_b = get(data, get(data, index + 2))
                elif b == 1:
                    result_b = get(data, index + 2)
                elif b == 2:
                    result_b = get(data, base + get(data, index + 2))
                result = result_c < result_b
                if a == 0:
                    set(data, get(data, index + 3), result)
                elif a == 1:
                    set(data, index + 3, result)
                elif a == 2:
                    set(data, base + get(data, index + 3), result)
                index += 4
                # return
            elif de == 8:
                # result = int(get(data, index + 1) if c else get(data, get(data, index + 1))) == int(get(data, index + 2) if b else get(data, get(data, index + 2)))
                if c == 0:
                    result_c = get(data, get(data, index + 1))
                elif c == 1:
                    result_c = get(data, index + 1)
                elif c == 2:
                    result_c = get(data, base + get(data, index + 1))
                if b == 0:
                    result_b = get(data, get(data, index + 2))
                elif b == 1:
                    result_b = get(data, index + 2)
                elif b == 2:
                    result_b = get(data, base + get(data, index + 2))
                result = result_c == result_b
                if a == 0:
                    set(data, get(data, index + 3), result)
                elif a == 1:
                    set(data, index + 3, result)
                elif a == 2:
                    set(data, base + get(data, index + 3), result)
                index += 4
                # return
            elif de == 9:
                # print 'processing X09:', c, index + 1, 'test', data[index + 1], 'check', get(data, index + 1)
                if c == 0:
                    base += get(data, get(data, index + 1))
                elif c == 1:
                    base += get(data, index + 1)
                elif c == 2:
                    base += get(data, base + get(data, index + 1))
                index += 2
                # return
            else:
                print 'de unknown:', de
                return

            # print 'out:', data, 'index:', index, 'base:', base, '_input:', _input
    # process_opcode(data, index, base, _input)

def main():
    fp = open(input_file)
    data = [int(i) for i in fp.read().split(',')]
    process_opcode(data, 1)

    # data = [int(i) for i in '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'.split(',')]
    # process_opcode(data, 1)
    # data = [int(i) for i in '1102,34915192,34915192,7,4,7,99,0'.split(',')] # a 16-digit number
    # process_opcode(data, 1)
    # data = [int(i) for i in '104,1125899906842624,99'.split(',')] # 1125899906842624
    # process_opcode(data, 1)

    fp.close()

if __name__ == "__main__":
   main()