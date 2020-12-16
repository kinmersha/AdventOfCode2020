def part1():
    nums = []
    with open('day10/input') as f:
        for line in f:
            nums.append(int(line))

    nums.sort()

    diffs = {1: 0, 2: 0, 3: 0}
    
    diffs[nums[0]] += 1  # Get initial jump from 0 to first adapter
    for i in range(0, len(nums) - 1):
        diffs[nums[i + 1] - nums[i]] += 1
    diffs[3] += 1  # Your device adapter is always 3 higher than the last one
    
        
    print(f'Part 1 answer: {diffs[1] * diffs[3]}')


if __name__ == '__main__':
    part1()
