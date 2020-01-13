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
            # print paint
            # print len(paint)
            # print [tile[0:2] for tile in paint]
            # print len(set([tile[0:2] for tile in paint]))

            # print _input
            # print data

            # print paint

            cols = max([tile[0] for tile in paint]) - min([tile[0] for tile in paint])
            rows = max([tile[1] for tile in paint]) - min([tile[1] for tile in paint])

            paintjob = ['None'] * ((cols + 1) * (rows + 1))
            for tile in paint:
                # print len(paintjob), tile[0] + tile[1] * cols, tile[0], tile[1]
                paintjob[tile[0] + tile[1] * cols] = tile[2]
            for row in range(rows + 1):
                print ''.join([str(tile).replace('None', ' ').replace('0', ' ').replace('1', '#') for tile in paintjob[cols * row:cols * (row + 1)]])

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
    process_opcode(data, 1)
    fp.close()

if __name__ == "__main__":
   main()