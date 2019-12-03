#!/usr/bin/python
input_file = 'input.txt'

def unfold(wire):
    output = [(0, 0)]
    for step in wire:
        if (step[0] == 'U'):
            output.append((output[-1][0], output[-1][1] - step[1]))
        if (step[0] == 'D'):
            output.append((output[-1][0], output[-1][1] + step[1]))
        if (step[0] == 'L'):
            output.append((output[-1][0] - step[1], output[-1][1]))
        if (step[0] == 'R'):
            output.append((output[-1][0] + step[1], output[-1][1]))
    return output

def intersect(wire1, wire2):
    output = []
    steps1 = 0
    for i1 in range(1, len(wire1)):
        x1, x1p, y1, y1p = wire1[i1][0], wire1[i1 - 1][0], wire1[i1][1], wire1[i1 - 1][1]
        steps2 = 0
        for i2 in range(1, len(wire2)):
            x2, x2p, y2, y2p = wire2[i2][0], wire2[i2 - 1][0], wire2[i2][1], wire2[i2 - 1][1]
            intx = inty = None
            if x1 <= x2 <= x1p or x1p <= x2 <= x1:
                intx = x2
                s2 = abs(y1 - y2p)
            elif x2 <= x1 <= x2p or x2p <= x1 <= x2:
                intx = x1
                s1 = abs(y2 - y1p)
            if y1 <= y2 <= y1p or y1p <= y2 <= y1:
                inty = y2
                s2 = abs(x1 - x2p)
            elif y2 <= y1 <= y2p or y2p <= y1 <= y2:
                inty = y1
                s1 = abs(x2 - x1p)
            if intx and inty:
                output.append((intx, inty, steps1 + s1, steps2 + s2))
            steps2 = steps2 + abs(x2 - x2p) + abs(y2 - y2p)
        steps1 = steps1 + abs(x1 - x1p) + abs(y1 - y1p)
    return output

def main():
    fp = open(input_file)
    wire1, wire2 = [[(i[0], int(i.strip()[1:])) for i in row.split(',')] for row in fp.read().strip().split('\n')]
    # wire1, wire2 = [[(i[0], int(i.strip()[1:])) for i in row.split(',')] for row in ['R8,U5,L5,D3','U7,R6,D4,L4']] # 6 | 30
    # wire1, wire2 = [[(i[0], int(i.strip()[1:])) for i in row.split(',')] for row in ['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83']] # 159 | 610
    # wire1, wire2 = [[(i[0], int(i.strip()[1:])) for i in row.split(',')] for row in ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']] # 135 | 410
    wire1, wire2 = unfold(wire1), unfold(wire2)
    intersections = intersect(wire1, wire2)
    # print intersections
    # print min([abs(i[0]) + abs(i[1]) for i in intersections])
    print min([i[2] + i[3] for i in intersections])
    fp.close()

if __name__ == "__main__":
   main()