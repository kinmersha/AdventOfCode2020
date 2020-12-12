import itertools

def read_data(file):
    with open(f'day09/{file}') as f:
        nums = []
        for line in f:
            nums.append(int(line))
    return nums


def validate(nums, n):
    # For a list of integers and a preamble of length n, this function checks 
    # all numbers to see whether they follow the rule that they must be the sum 
    # of two unique numbers of the previous n elements.

    valid = [False] * (len(nums) - n)
    for i in range(n, len(nums)):
        pairs = itertools.combinations(nums[i - n:i], 2)
        for p in pairs:
            if sum(p) == nums[i] and p[0] != p[1]:
                valid[i - n] = True
    return valid


def part1():
    filename = 'input'
    prefix = 25
    nums = read_data(filename)
    valid = validate(nums, prefix)
    # List.index(elem) gives the index of the first occurence of elem
    print(f'Part 1 answer: {nums[prefix + valid.index(False)]}')


# Now we gotta do some dynamic programming; exciting! (weird to put an 
# exclamation right after a semicolon :D)

# Once again, we're gonna see how well I can pull this out of my ass based on 
# what I remember of my algorithms course from two years ago.

def find_run(nums, index):
    # Now we need to find a continuous run that sums to the key value (nums[index]).

    # Memory array (O(n))
    cum_sums = [0] * index
    # Approach: We iterate through the list from index i = 0 to n-, storing the
    # cumulative sum of a run of length k starting at index i in cum_sums[i]. As
    # we increase k by 1, we traverse now i = 0 to n-2, updating the sums, and
    # so on, until we reach a sum equal to key.

    # Looks like I was right in my guess that actually we should only iterate
    # over the subset of the list before the key.
    for k in range(1, index):
        for i in range(0, index - k + 1):  # Explicit lower bound to help my brain
            cum_sums[i] = cum_sums[i] + nums[i + k - 1]
            if cum_sums[i] == nums[index]:
                return i, k

# Pretty sure this should be doable in O(n^2) time.
def part2():
    # First, we need our answer from part 1
    filename = 'input'
    prefix = 25
    nums = read_data(filename)
    valid = validate(nums, prefix)
    
    i, k = find_run(nums, prefix + valid.index(False))
    
    # Now we need the sum of the largest and smallest elements of the run
    ans = min(nums[i:i + k - 1]) + max(nums[i:i + k - 1])
    print(f'Part 2 answer: {ans}')

    # Damn, I actually puzzled out how to do this DP program right on the first 
    # try, the only thing that fucked me up was that just putting one break 
    # didn't exit the whole loop, so it's python's fault, and woulda been no 
    # issue if i just made it a function in the first place 😔
    #
    # Well, testing on the the little baby example was helpful for both of 
    # these, but getting right answer on the big question first time made me 
    # very happy.


if __name__ == '__main__':
    part1()
    part2()
