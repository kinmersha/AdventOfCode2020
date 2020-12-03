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
    # print(field.mat)
    numTrees = 0
    for row in range(1, field.height):
        col = 3*row
        numTrees += field.isTree(row, col)

    print(f'Part 1 answer: {numTrees}')

# def part2():
#     passwords = [Part2Password(p) for p in read_data()]
#     tf = [p.isValid() for p in passwords]
#     print(f'Part 1 answer: {sum(tf)}')



if __name__ == '__main__':
    part1()
    # part2()
