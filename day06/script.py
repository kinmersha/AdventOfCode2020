def part1():
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

    print(f'Part 1 answer: {sum((len(s) for s in group_counts))}')


# Even more set fun! Now we need to look at set intersections, which requires 
# a modified version of the data-parsing, which is why I deleted the read_data()
# function, since the code wasn't resuable.
def part2():
    with open('day06/input') as f:
        group_counts = []
        combo = ''
        for line in f:
            if line == '\n':
                temp = [set((q for q in person)) for person in combo.split()]
                # Use * 'splat' operator to get intersection of list of sets
                group_counts.append(set.intersection(*temp))
                combo = ''
            else:
                # Join on spaces to keep each line--each person--distinct.
                combo = ' '.join([combo, line.strip()])
    # Get last group
    temp = [set((q for q in person)) for person in combo.split()]
    group_counts.append(set.intersection(*temp))

    print(f'Part 2 answer: {sum((len(s) for s in group_counts))}')


if __name__ == '__main__':
    part1()
    part2()