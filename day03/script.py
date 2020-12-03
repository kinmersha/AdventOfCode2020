import math
from abc import abstractmethod

TREE_CHAR = '#'

class Field:
    def __init__(self, filename):
        with open(filename) as f:
            lines = []
            for line in f:
                lines.append(line.strip())

        # Store tree map as a boolean array
        self.width = len(lines[0])
        self.height = len(lines)
        self.mat = [[False] * self.width] * self.height
        for i in range(self.height):
            self.mat[i] = [x == '#' for x in lines[i]]
            # WHY DOES THIS NOT WORK (makes everything true):
            # for j in range(self.width):
            #     if lines[i][j] == "#":
            #         self.mat[i][j] = True
    
    def isTree(self, row, col):
        # Wrap column bc the map tiles
        return self.mat[row][col % self.width]


def part1():
    field = Field('day03/input')
    numTrees = 0
    for row in range(1, field.height):
        col = 3*row
        numTrees += field.isTree(row, col)

    print(f'Part 1 answer: {numTrees}')

def traverse(field, slope):
    dx, dy = slope #unpack
    x = 0  # start
    y = 0
    numTrees = 0
    while y < field.height:
        numTrees += field.isTree(y, x)
        x += dx
        y += dy
    
    return numTrees

def part2():
    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    field = Field('day03/input')

    trees = []
    for slope in slopes:
        trees.append(traverse(field, slope))
        print(f'For slope right {slope[0]}, down {slope[1]}: hit {trees[-1]} trees')

    print(f'Part 2 answer: {math.prod(trees)}')



if __name__ == '__main__':
    part1()
    part2()
