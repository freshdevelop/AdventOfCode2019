#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
input_file = 'input.txt'

def get_(data, position):
    return int(data[position]) if position < len(data) else 0

def set_(data, position, value): # https://stackoverflow.com/questions/22388866/python-list-set-value-at-index-if-index-does-not-exist
    try:
        data[position] = value
    except IndexError:
        for _ in range(position - len(data) + 1):
            data.append(None)
        set_(data, position, value)
    
def updatepaint(paint, position, _input):
    # print 'updatepaint', position, _input
    paint.append((position[0], position[1], _input)) # x, y, color (0: black  1: white)
    return paint

def updateposition(position, _input):
    # print 'updateposition', position, _input
    if not _input: # turn left
        if position[2] % 4 == 0:   # N > W
            return (position[0] - 1, position[1], position[2] - 1)
        elif position[2] % 4 == 1: # E > N
            return (position[0], position[1] - 1, position[2] - 1)
        elif position[2] % 4 == 2: # S > E
            return (position[0] + 1, position[1], position[2] - 1)
        elif position[2] % 4 == 3: # W > S
            return (position[0], position[1] + 1, position[2] - 1)
    else: # turn right
        if position[2] % 4 == 0:   # N > E
            return (position[0] + 1, position[1], position[2] + 1)
        elif position[2] % 4 == 1: # E > S
            return (position[0], position[1] + 1, position[2] + 1)
        elif position[2] % 4 == 2: # S > W
            return (position[0] - 1, position[1], position[2] + 1)
        elif position[2] % 4 == 3: # W > N
            return (position[0], position[1] - 1, position[2] + 1)

def process_opcode(data, _input):
    index = 0
    base = 0
    mode = 0 # 0: paint  1: turn
    position = (0, 0, 0) # x, y, direction (0: N  1: E  2: S  3: W)
    paint = []
    while True:
        # print 'index:', index, data[index], '_input:', _input
        # if index > 100:
        #     return

        if data[index] == 1:
            # print 'processing 1:', data[index : index + 4]
            set_(data, get_(data, index + 3), get_(data, get_(data, index + 1)) + get_(data, get_(data, index + 2)))
            index += 4
            # return
        elif data[index] == 2:
            # print 'processing 2:', data[index : index + 4]
            set_(data, get_(data, index + 3), get_(data, get_(data, index + 1)) * get_(data, get_(data, index + 2)))
            index += 4
            # return
        elif data[index] == 3:
            # print 'processing 3:', data[index : index + 2]
            set_(data, get_(data, index + 1), _input)
            index += 2
            # return
        elif data[index] == 4:
            # print 'processing 4:', data[index : index + 2]
            _input = get_(data, get_(data, index + 1))
            
            # print 'output', _input
            if not mode: # paint
                paint = updatepaint(paint, position, _input)
            else: # turn, move
                position = updateposition(position, _input)
                matches = [tile for tile in paint if tile[0:2] == position[0:2]]
                _input = matches[-1][2] if matches else 0
            mode = not mode

            index += 2
            # return
        elif data[index] == 5:
            # print 'processing 5:', data[index : index + 2]
            index = get_(data, index + 2) if get_(data, index + 1) else index + 2
            # return
        elif data[index] == 6:
            # print 'processing 6:', data[index : index + 2]
            index = get_(data, index + 2) if not get_(data, index + 1) else index + 2
            # return
        elif data[index] == 7:
            # print 'processing 7:', data[index : index + 4]
            set_(data, get_(data, index + 3), get_(data, get_(data, index + 1)) < get_(data, get_(data, index + 2)))
            index += 4
            # return
        elif data[index] == 8:
            # print 'processing 8:', data[index : index + 4]
            set_(data, get_(data, index + 3), get_(data, get_(data, index + 1)) == get_(data, get_(data, index + 2)))
            index += 4
            # return
        elif data[index] == 9:
            # print 'processing 9:', data[index : index + 2]
            base += get_(data, get_(data, index + 1))
            index += 2
            # return
        elif data[index] == 99:
            print paint
            # print len(paint)
            # print [tile[0:2] for tile in paint]
            print len(set([tile[0:2] for tile in paint]))

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
                # result = int(get_(data, index + 1) if c else get_(data, get_(data, index + 1))) + int(get_(data, index + 2) if b else get_(data, get_(data, index + 2)))
                if c == 0:
                    result_c = get_(data, get_(data, index + 1))
                elif c == 1:
                    result_c = get_(data, index + 1)
                elif c == 2:
                    result_c = get_(data, base + get_(data, index + 1))
                if b == 0:
                    result_b = get_(data, get_(data, index + 2))
                elif b == 1:
                    result_b = get_(data, index + 2)
                elif b == 2:
                    result_b = get_(data, base + get_(data, index + 2))
                result = result_c + result_b
                if a == 0:
                    set_(data, get_(data, index + 3), result)
                elif a == 1:
                    set_(data, index + 3, result)
                elif a == 2:
                    set_(data, base + get_(data, index + 3), result)
                index += 4
                # return
            elif de == 2:
                # result = int(get_(data, index + 1) if c else get_(data, get_(data, index + 1))) * int(get_(data, index + 2) if b else get_(data, get_(data, index + 2)))
                if c == 0:
                    result_c = get_(data, get_(data, index + 1))
                elif c == 1:
                    result_c = get_(data, index + 1)
                elif c == 2:
                    result_c = get_(data, base + get_(data, index + 1))
                if b == 0:
                    result_b = get_(data, get_(data, index + 2))
                elif b == 1:
                    result_b = get_(data, index + 2)
                elif b == 2:
                    result_b = get_(data, base + get_(data, index + 2))
                result = result_b * result_c
                if a == 0:
                    set_(data, get_(data, index + 3), result)
                elif a == 1:
                    set_(data, index + 3, result)
                elif a == 2:
                    set_(data, base + get_(data, index + 3), result)
                # print result_b, result_c, result
                # print get_(data, index + 3)
                index += 4
                # print data
                # return
            elif de == 3:
                if c == 0:
                    set_(data, get_(data, index + 1), _input)
                elif c == 1:
                    set_(data, index + 1, _input)
                elif c == 2:
                    set_(data, base + get_(data, index + 1), _input)
                    # print 'writing', _input, 'at position', base + get_(data, index + 1)
                index += 2
                # return
            elif de == 4:
                if c == 0:
                    _input = get_(data, get_(data, index + 1))
                elif c == 1:
                    _input = get_(data, index + 1)
                elif c == 2:
                    _input = get_(data, base + get_(data, index + 1))
                
                # print 'output', _input
                if not mode: # paint
                    paint = updatepaint(paint, position, _input)
                else: # turn, move
                    position = updateposition(position, _input)
                    matches = [tile for tile in paint if tile[0:2] == position[0:2]]
                    _input = matches[-1][2] if matches else 0
                mode = not mode

                index += 2
                # return
            elif de == 5:
                # index = int(get_(data, index + 2) if b else get_(data, get_(data, index + 2))) if int(get_(data, index + 1) if c else get_(data, get_(data, index + 1))) else index + 3
                if c == 0:
                    result_c = get_(data, get_(data, index + 1))
                elif c == 1:
                    result_c = get_(data, index + 1)
                elif c == 2:
                    result_c = get_(data, base + get_(data, index + 1))
                if result_c:
                    if b == 0:
                        index = get_(data, get_(data, index + 2))
                    elif b == 1:
                        index = get_(data, index + 2)
                    elif b == 2:
                        index = get_(data, base + get_(data, index + 2))
                else:
                    index += 3
                # return
            elif de == 6:
                # index = int(get_(data, index + 2) if b else get_(data, get_(data, index + 2))) if not int(get_(data, index + 1) if c else get_(data, get_(data, index + 1))) else index + 3
                if c == 0:
                    result_c = get_(data, get_(data, index + 1))
                elif c == 1:
                    result_c = get_(data, index + 1)
                elif c == 2:
                    result_c = get_(data, base + get_(data, index + 1))
                if not result_c:
                    if b == 0:
                        index = get_(data, get_(data, index + 2))
                    elif b == 1:
                        index = get_(data, index + 2)
                    elif b == 2:
                        index = get_(data, base + get_(data, index + 2))
                else:
                    index += 3
                # return
            elif de == 7:
                # result = int(get_(data, index + 1) if c else get_(data, get_(data, index + 1))) < int(get_(data, index + 2) if b else get_(data, get_(data, index + 2)))
                if c == 0:
                    result_c = get_(data, get_(data, index + 1))
                elif c == 1:
                    result_c = get_(data, index + 1)
                elif c == 2:
                    result_c = get_(data, base + get_(data, index + 1))
                if b == 0:
                    result_b = get_(data, get_(data, index + 2))
                elif b == 1:
                    result_b = get_(data, index + 2)
                elif b == 2:
                    result_b = get_(data, base + get_(data, index + 2))
                result = result_c < result_b
                if a == 0:
                    set_(data, get_(data, index + 3), result)
                elif a == 1:
                    set_(data, index + 3, result)
                elif a == 2:
                    set_(data, base + get_(data, index + 3), result)
                index += 4
                # return
            elif de == 8:
                # result = int(get_(data, index + 1) if c else get_(data, get_(data, index + 1))) == int(get_(data, index + 2) if b else get_(data, get_(data, index + 2)))
                if c == 0:
                    result_c = get_(data, get_(data, index + 1))
                elif c == 1:
                    result_c = get_(data, index + 1)
                elif c == 2:
                    result_c = get_(data, base + get_(data, index + 1))
                if b == 0:
                    result_b = get_(data, get_(data, index + 2))
                elif b == 1:
                    result_b = get_(data, index + 2)
                elif b == 2:
                    result_b = get_(data, base + get_(data, index + 2))
                result = result_c == result_b
                if a == 0:
                    set_(data, get_(data, index + 3), result)
                elif a == 1:
                    set_(data, index + 3, result)
                elif a == 2:
                    set_(data, base + get_(data, index + 3), result)
                index += 4
                # return
            elif de == 9:
                # print 'processing X09:', c, index + 1, 'test', data[index + 1], 'check', get_(data, index + 1)
                if c == 0:
                    base += get_(data, get_(data, index + 1))
                elif c == 1:
                    base += get_(data, index + 1)
                elif c == 2:
                    base += get_(data, base + get_(data, index + 1))
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
    process_opcode(data, 0)
    fp.close()

    # https://pastebin.com/47bKDe0H
    # https://www.reddit.com/r/adventofcode/comments/e96ywo/2019_day_11_part_1_what_am_i_doing_wrong/
    # data = [int(i) for i in '3,8,1005,8,334,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,28,2,1108,5,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,55,1,102,18,10,1,2,5,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,84,1,106,11,10,2,1008,6,10,1,4,4,10,1006,0,55,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,121,1,107,9,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,147,2,1002,4,10,2,104,18,10,1,107,16,10,1,108,8,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,185,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,208,2,1009,16,10,1006,0,7,1006,0,18,1,1105,8,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,243,2,1105,20,10,2,106,10,10,1006,0,67,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,276,2,1103,5,10,2,1104,7,10,1006,0,35,2,1105,3,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,314,101,1,9,9,1007,9,1097,10,1005,10,15,99,109,656,104,0,104,1,21102,936995824532,1,1,21101,0,351,0,1105,1,455,21102,1,387508445964,1,21102,362,1,0,1106,0,455,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,235244973059,1,21101,409,0,0,1106,0,455,21102,179410541659,1,1,21101,0,420,0,1105,1,455,3,10,104,0,104,0,3,10,104,0,104,0,21101,868402070292,0,1,21102,1,443,0,1106,0,455,21102,1,709584749324,1,21102,454,1,0,1106,0,455,99,109,2,22102,1,-1,1,21101,40,0,2,21102,486,1,3,21101,0,476,0,1106,0,519,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,481,482,497,4,0,1001,481,1,481,108,4,481,10,1006,10,513,1101,0,0,481,109,-2,2106,0,0,0,109,4,2102,1,-1,518,1207,-3,0,10,1006,10,536,21102,0,1,-3,21202,-3,1,1,22102,1,-2,2,21102,1,1,3,21102,555,1,0,1106,0,560,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,583,2207,-4,-2,10,1006,10,583,21201,-4,0,-4,1106,0,651,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,602,1,0,1106,0,560,22102,1,1,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,621,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,643,21201,-1,0,1,21102,643,1,0,106,0,518,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0'.split(',')]
    # process_opcode(data, 0)

if __name__ == "__main__":
   main()