#!/usr/bin/python
import math
input_file = 'input.txt'

def count_sightings(asteroids, i):
    current = asteroids[i]
    relative = [tuple(map(int.__sub__, asteroid, current)) for asteroid in asteroids if asteroid is not current] # imposto l'asteroide corrente come punto 0, 0
    theta = [math.atan2(asteroid[1], asteroid[0]) for asteroid in relative] # calcolo la direzione in radianti per ciascuno degli altri asteroidi, ne tengo uno solo per ciascuna direzione
    return len(set(theta))

def shoot_laser(asteroids, reference, target):
    current = asteroids[reference]
    relative = [tuple(map(int.__sub__, asteroid, current)) for asteroid in asteroids if asteroid is not current]
    # theta = [math.atan2(asteroid[1], asteroid[0]) for asteroid in relative]
    theta = [-math.atan2(asteroid[1], asteroid[0]) - math.pi / 2 for asteroid in relative]
    theta = [t if t < 0.0000000000000000001 else -(math.pi * 2) + t for t in theta]
    theta = [-t for t in theta]
    distance = [math.sqrt(asteroid[0] ** 2 + asteroid[1] ** 2) for asteroid in relative]
    ordered = zip(theta, distance, relative)
    ordered.sort()
    # for o in ordered:
    #     # exploded = (current[0] + o[2][0], current[1] + o[2][1])
    #     # print exploded, o[0], o[1]
    #     print o[0], o[1], (current[0] + o[2][0], current[1] + o[2][1])
    # print '-' * 5

    # relative = [tuple(map(int.__sub__, asteroid, current)) for asteroid in asteroids if asteroid is not current]
    # # # theta = [math.atan2(asteroid[1], asteroid[0]) for asteroid in relative]
    # theta = [((math.atan2(asteroid[1], asteroid[0]) - math.pi / 2) % (math.pi * 2)) for asteroid in relative]
    # # # theta = [(math.pi * 2 - (math.atan2(asteroid[1], asteroid[0]) - math.pi / 2) % (math.pi * 2) % math.pi) for asteroid in relative]
    # distance = [math.sqrt(asteroid[0] ** 2 + asteroid[1] ** 2) for asteroid in relative]
    # # # print len(theta), len(distance), len(relative)
    # ordered = zip(theta, distance, relative)

    # ordered.sort()
    # for o in ordered:
    #     print o
    # print '-' * 5
    # # exploded = ordered[0]
    # # print current, exploded
    # # print (current[0] + exploded[2][0], current[1] + exploded[2][1])

    i = 0
    current_theta = None
    while i <= target:
        while ordered[i][0] == current_theta:
            # print 'skip', ordered[i]
            ordered.append(ordered.pop(0))
        exploded = ordered[i]
        # print i, ':', exploded, (current[0] + exploded[2][0], current[1] + exploded[2][1])
        if i == target:
            print (current[0] + exploded[2][0]) * 100 + (current[1] + exploded[2][1])
        current_theta = exploded[0]
        i += 1

    # # for t in theta:
    # #     print t, (math.pi * 2 - t) % math.pi
    # # print theta
    # # print '-' * 5
    # # print distance
    # # shift = math.atan2(1, 0)
    # # print shift
    # # # print (math.atan2(1, 1) - math.pi / 2) % (math.pi * 2)
    # # print (math.atan2(1, 0) - math.pi / 2) % (math.pi * 2)
    # # # print (math.atan2(1, -1) - math.pi / 2) % (math.pi * 2)
    # # print (math.atan2(0, -1) - math.pi / 2) % (math.pi * 2)
    # # print (math.atan2(-1, 0) - math.pi / 2) % (math.pi * 2)
    # # print (math.atan2(0, 1) - math.pi / 2) % (math.pi * 2)

    # # print min(theta), max(theta)

def main():
    fp = open(input_file)
    data = fp.read()
    fp.close()
    
#     data = """
# .#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##
# """

    data = [row for row in data.split("\n") if row]
    asteroids = [(col_i, row_i) for row_i in range(len(data)) for col_i in range(len(data[row_i])) if data[row_i][col_i] == '#']
    sightings = [count_sightings(asteroids, i) for i in range(len(asteroids))]
    reference = sightings.index(max(sightings))
    # print reference, asteroids[reference]

    shoot_laser(asteroids, reference, 199)
    

if __name__ == "__main__":
   main()