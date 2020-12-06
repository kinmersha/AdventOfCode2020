class BoardingPass:
    def __init__(self, t):
        t = t.replace('B', '1')
        t = t.replace('R', '1')
        t = t.replace('F', '0')
        t = t.replace('L', '0')

        self.row = int(t[0:7], 2)  # Base-2 -> convert binary to decimal
        self.col = int(t[7:], 2)
    
    def getID(self):
        return 8 * self.row + self.col
        

def readPasses():
    with open('day05/input') as f:
        passes = []
        for line in f:
            passes.append(BoardingPass(line.strip()))
    
    return passes


def part1():
    passes = readPasses()
    print(f'Part 1 answer: {max((p.getID() for p in passes))}')


def part2():
    passes = readPasses()
    passes.sort(key=lambda p: p.getID())

    # We know some IDs at the beginning and end of the range are
    # missing, but since we sorted it, we just look for the one
    # gap in the list.
    for i in range(1, len(passes)):
        if passes[i].getID() - passes[i - 1].getID() > 1:  # Found it!
            print(f'Part 2 answer: {passes[i].getID()-1}')
            return


if __name__ == '__main__':
    part1()
    part2()