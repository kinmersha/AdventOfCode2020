import math

def part1():
    passports = []
    combo = "" # For sexy oneliner later
    with open('day04/input') as f:
        for line in f:
            if line == '\n': # break between passports
                passports.append({x.split(':')[0]: x.split(':')[1] 
                                  for x in combo.split()})
                combo = ""
            else: # Build up 
                combo = ' '.join([combo, line])
    # Don't lose the last passport
    passports.append({x.split(':')[0]: x.split(':')[1]
                      for x in combo.split()})

    valid = 0
    for pp in passports:
        if len(pp) == 8: # all fields
            valid += 1
        elif len(pp) == 7:  # doesn't need cid
            if "cid" not in pp.keys():
                valid += 1

    print(f'Part 1 answer: {valid}')




if __name__ == '__main__':
    part1()
    # part2()
