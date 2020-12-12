def execute(lines, visited, i, acc):
    # This function executes normally like in part 1
    while i < len(lines):
        if visited[i]:
            return ("no good :(", acc)
        else:
            visited[i] = True
            op, addr = lines[i].strip().split()
            addr = int(addr)

            if op == 'nop':
                i += 1  # Continue to next instruction
            elif op == 'acc':
                acc += addr
                i += 1
            else:  # jump
                i += addr

    if i == len(lines):  # We found a version that exits!
        return (acc, acc)
    else:
        return ("no good :(", acc)


def part1():
    with open(f'day08/input') as f:
        lines = f.readlines()

        visited = [False] * len(lines)
        i = 0
        acc = 0
        ans, acc = execute(lines, visited, i, acc)
                
    print(f'Part 1 answer: {acc}')


# Now we need to find exactly one instruction to change so that the file will
# terminate. Either switch a nop to a jmp, or visa-versa. The program terminates
# by trying to advance to the instruction after the last one in the file.

# Attempt to solve by greedy search (just try changing each jmp/nop we encounter 
# and see if that gets us to the program exit state).
def part2():
    with open(f'day08/input') as f:
        lines = f.readlines()

        visited = [False] * len(lines)
        i = 0
        acc = 0
        while not visited[i]:
            visited[i] = True
            op, addr = lines[i].strip().split()
            addr = int(addr)

            if op == 'nop':
                # check alternate version
                var_lines = lines.copy()
                var_lines[i] = f'jmp {addr:+}'
                var_visited = visited.copy()
                var_visited[i] = False
                ans, acc = execute(var_lines, var_visited, i, acc)
                if ans != 'no good :(':
                    break

                # Otherwise, we keep going and will keep trying til we find the 
                # right instruction to change
                i += 1
            elif op == 'acc':
                acc += addr
                i += 1
            else:  # jump
                # check alternate version
                var_lines = lines.copy()
                var_lines[i] = f'nop {addr:+}'
                var_visited = visited.copy()
                var_visited[i] = False
                ans, acc = execute(var_lines, var_visited, i, acc)
                if ans != 'no good :(':
                    break

                # Otherwise, we keep going and will keep trying til we find the
                # right instruction to change
                i += addr

    print(f'Part 2 answer: {acc}')
    

if __name__ == '__main__':
    part1()
    part2()
