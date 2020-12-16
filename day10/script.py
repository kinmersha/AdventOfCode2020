import collections

def read_input():
    nums = [0]  # Wall starts at 0 jolts
    with open('day10/input') as f:
        for line in f:
            nums.append(int(line))

    nums.append(max(nums) + 3)  # Your device is always a +3 jump from the end
    return sorted(nums)


def diffs(nums):
    return [j - i for i, j in zip(nums[:-1], nums[1:])]


def part1():
    nums = read_input()

    diff_counts = collections.Counter(diffs(nums))
        
    print(f'Part 1 answer: {diff_counts[1] * diff_counts[3]}')


# There are list permutation possibilities whenever two or more 1-jolt jumps 
# happen in a row. How to count these effectively...

# I cheated and looked online bc I felt it was too stupid to try and brute force 
# it recursively, but I saw at least one other person do that, so I'll try it 
# now.

# Realized I didn't rly know how to do it recursively and I couldn't even make
# sense of the solution I'd found, looked at some others and there're really 
# clean memoized solutions :weary:


def part2():
    nums = read_input()

    # There is 1 possible path starting from the wall (we have to use the wall
    # socket)
    # We use a counter bc it defaults the value of a key to 0 rather than 
    # throwing an error for accessing an un-set key.
    paths = collections.Counter({0: 1})

    for x in nums:
        # If there is an adapter 1 jolt higher than adapter x, then all paths to
        # x can get to it.
        paths[x + 1] += paths[x]
        # Same if there is an adapter 2 jolts higher.
        paths[x + 2] += paths[x]
        paths[x + 3] += paths[x]
        # If there is no adapter that exists for one or two of these jumps, it 
        # doesn't matter, bc we'll never access the value stored there.

    print(f'Part 2 answer: {paths[max(nums)]}')


if __name__ == '__main__':
    part1()
    part2()