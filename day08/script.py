def part1():
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
                i += 1  # Continue to next instruction
            elif op == 'acc':
                acc += addr
                i += 1
            else:  # jump
                i += addr
                
    print(f'Part 1 answer: {acc}')
    

if __name__ == '__main__':
    part1()
