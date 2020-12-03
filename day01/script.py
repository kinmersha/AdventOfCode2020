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
    
if __name__ == '__main__':
    part1_lazy()
