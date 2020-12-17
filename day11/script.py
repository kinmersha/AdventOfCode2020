import itertools

class Arena:
    def __init__(self, filename):
        with open(filename) as f:
            lines = f.readlines()
        grid = []
        for line in lines:
            grid.append([self.convert(c) for c in line.strip()])
        
        self.grid = grid
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.rounds = 0
        self.thresh = 4  # Number of surrounding seats occupied for person to leave

    def convert(self, c):
        if c == '.':
            return - 1
        elif c == 'L':
            return 0
        else:  # '#'
            return 1

    def check(self, row, col):
        # Return the number of occupied seats adjacent to (row, col)
        top = max(row - 1, 0)
        # +2 on the far bound bc it's exclusive
        bot = min(row + 2, self.height)
        left = max(col - 1, 0)
        right = min(col + 2, self.width)

        # Build slice view of grid, this max 3x3 so very fast
        count = 0
        for i in range(top, bot):
            for j in range(left, right):
                if not(i == row and j == col):
                    count += self.grid[i][j] == 1
        
        return count

    def grids_equal(self, next_grid):
        for i in range(self.height):
            for j in range(self.width):
                if next_grid[i][j] != self.grid[i][j]:
                    return False
        return True

    def update(self):
        next_grid = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if self.grid[i][j] == -1:  # Floor
                    row.append(-1)
                elif self.grid[i][j] == 0:  # Empty seat
                    # If there are no neighbors, fill it
                    row.append(self.check(i, j) == 0)
                else:  # Full seat
                    row.append(not (self.check(i, j) >= self.thresh))
            next_grid.append(row)

        
        if self.grids_equal(next_grid):
            return False
        else:
            self.rounds += 1
            self.grid = next_grid
            return True

    def get_seat_count(self):
        return sum((x > 0 for x in itertools.chain.from_iterable(self.grid)))

    def print_grid(self):
        for row in self.grid:
            line = ""
            for c in row:
                if c == -1:
                   line += '.'
                elif c == 0:
                    line += 'L'
                else:
                    line += '#'
            print(line)
        print()  # Trailing newline
        

def part1():
    arena = Arena('day11/input')

    # arena.print_grid()
    while arena.update():
        # arena.print_grid()
        pass

    print(f'Part 1 answer: {arena.get_seat_count()}')


# Get all "looking" direction vectors plus the stationary vector (0, 0)
deltas = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
deltas.remove((0, 0))


class P2Arena(Arena):
    def creep(self, r, c, dr, dc):
        # Creep from the start point in the direction pointed to by the delta 
        # vector (dr, dc) (delta row, delta column), until it either hits an
        # occupied seat or the edge of the frame.
        while True:
            r += dr
            c += dc
            if r < 0 or r >= self.height: # Didn't hit anything
                return 0
            elif c < 0 or c >= self.width:
                return 0
            elif self.grid[r][c] == 1: # Hit an occupied seat
                return 1
            elif self.grid[r][c] == 0:  # Hit an empty seat
                return 0
            # Otherwise keep creeping

    def check(self, row, col):
        # Overwrite check method for new "looking" behavior
        count = 0
        for d in deltas:
            count += self.creep(row, col, d[0], d[1])

        return count
        

def part2():
    # Write P2Arena class, just needs to override self.check() and set self.thresh = 5
    arena = P2Arena('day11/input')
    arena.thresh = 5

    # arena.print_grid()
    while arena.update():
        # arena.print_grid()
        pass

    print(f'Part 2 answer: {arena.get_seat_count()}')


if __name__ == '__main__':
    part1()
    part2()
