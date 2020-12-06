def read_data():
    with open('day06/input') as f:
        group_counts = []
        combo = ''
        for line in f:
            if line == '\n':  # End of group
                # We want to count unique appearances -> use a set!
                group_counts.append(set([c for c in combo]))
                combo = ''
            else:
                combo = ''.join([combo, line.strip()])
    # Get last group
    group_counts.append(set([c for c in combo]))

    return group_counts


def part1():
    group_counts = read_data()

    print(f'Part 1 answer: {sum((len(s) for s in group_counts))}')




if __name__ == '__main__':
    part1()
