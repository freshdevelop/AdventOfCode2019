#!/usr/bin/python
import math
input_file = 'input.txt'

def count_sightings(asteroids, i):
    # print i
    current = asteroids[i]
    relative = [tuple(map(int.__sub__, asteroid, current)) for asteroid in asteroids if asteroid is not current] # imposto l'asteroide corrente come punto 0, 0
    # print relative
    theta = [math.atan2(asteroid[1], asteroid[0]) for asteroid in relative] # calcolo la direzione in radianti per ciascuno degli altri asteroidi, ne tengo uno solo per ciascuna direzione
    # print theta[6], theta[7], theta[6] == theta[7]
    # print set(theta)
    # print len(set(theta))
    return len(set(theta))


def main():
    fp = open(input_file)
    data = fp.read()
    fp.close()
    
#     data = """
# .#..#
# .....
# #####
# ....#
# ...##
# """

#     data = """
# ......#.#.
# #..#.#....
# ..#######.
# .#.#.###..
# .#..#.....
# ..#....#.#
# #..#....#.
# .##.#..###
# ##...#..#.
# .#....####
# """

#     data = """
# #.#...#.#.
# .###....#.
# .#....#...
# ##.#.#.#.#
# ....#.#.#.
# .##..###.#
# ..#...##..
# ..##....##
# ......#...
# .####.###.
# """

#     data = """
# .#..#..###
# ####.###.#
# ....###.#.
# ..###.##.#
# ##.##.#.#.
# ....###..#
# ..#.#..#.#
# #..#.#.###
# .##...##.#
# .....#.#..
# """

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
    # print data
    asteroids = [(col_i, row_i) for row_i in range(len(data)) for col_i in range(len(data[row_i])) if data[row_i][col_i] == '#']
    print max([count_sightings(asteroids, i) for i in range(len(asteroids))])
    # count_sightings(asteroids, 0)
    # count_sightings(asteroids, 1)

if __name__ == "__main__":
   main()