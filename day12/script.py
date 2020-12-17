from math import cos, sin, pi

def read_data(filename):
    with open(filename) as f:
        return [(line[0], int(line[1:])) for line in f.readlines()]

def move(x, y, dist, bearing):
    newX = x + int(round(dist * cos(pi * bearing / 180)))
    newY = y + int(round(dist * sin(pi * bearing / 180)))
    return newX, newY
    

def part1():
    x, y = 0, 0
    heading = 0  # 0deg = east = +x
    bearings = {'N': 90, 'E': 0, 'S': -90, 'W': 180}

    commands = read_data('day12/input')
    for c in commands:
        if c[0] in bearings:
            x, y = move(x, y, c[1], bearings[c[0]])
        elif c[0] == 'F':
            x, y = move(x, y, c[1], heading)
        elif c[0] == 'L':
            heading += c[1]
        else:  # 'R'
            heading -= c[1]

    # Answer is manhattan distance traveled
    print(f'Part 1 answer: {abs(x) + abs(y)}')


def rotation(x, y, deg):
    rad = deg * pi / 180
    newX = int(round(x * cos(rad) - y * sin(rad)))
    newY = int(round(x * sin(rad) + y * cos(rad)))
    return newX, newY

def part2():
    # Waypoint is relative to the ship, forward moves ship along multiples of 
    # the waypoint vector, other move the waypoint relative to the ship.
    x, y = 0, 0
    waypoint = (10, 1)
    bearings = {'N': 90, 'E': 0, 'S': -90, 'W': 180}

    commands = read_data('day12/input')
    for c in commands:
        if c[0] in bearings:
            waypoint = move(waypoint[0], waypoint[1], c[1], bearings[c[0]])
        elif c[0] == 'F':
            x, y = x + waypoint[0] * c[1], y + waypoint[1] * c[1]
        elif c[0] == 'L':
            waypoint = rotation(waypoint[0], waypoint[1], c[1])
        else:  # 'R'
            waypoint = rotation(waypoint[0], waypoint[1], -c[1])

    # Answer is manhattan distance traveled
    print(f'Part 2 answer: {abs(x) + abs(y)}')


if __name__ == '__main__':
    part1()
    part2()