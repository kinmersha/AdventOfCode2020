magic_num = 2020

def part1_lazy():
    with open('day01/input') as f:
        nums = []
        for line in f:
            nums.append(int(line.strip()))
    
    for a in range(len(nums)):
        for b in range(a, len(nums)):
            if nums[a] + nums[b] == magic_num:
                print(f'Part 1 answer: {nums[a]*nums[b]}')
                return

def part2_lazy():
    import math
    from itertools import combinations

    with open('day01/input') as f:
        nums = []
        for line in f:
            nums.append(int(line.strip()))

    # Combinations of length 3
    comb = combinations(nums, 3)
    for c in comb:
        if sum(c) == magic_num:
            print(f'Part 2 answer: {math.prod(c)}')
            return
    
if __name__ == '__main__':
    part1_lazy()
    part2_lazy()
