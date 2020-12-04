import re


def read_passports():
    passports = []
    combo = ""  # For sexy oneliner later
    with open('day04/input') as f:
        for line in f:
            if line == '\n':  # break between passports
                passports.append({x.split(':')[0]: x.split(':')[1]
                                  for x in combo.split()})
                combo = ""
            else:  # Build up
                combo = ' '.join([combo, line])
    # Don't lose the last passport
    passports.append({x.split(':')[0]: x.split(':')[1]
                      for x in combo.split()})
    return passports


def part1():
    passports = read_passports()

    valid = 0
    for pp in passports:
        if len(pp) == 8: # all fields
            valid += 1
        elif len(pp) == 7:  # doesn't need cid
            if "cid" not in pp.keys():
                valid += 1

    print(f'Part 1 answer: {valid}')


def valid_pp(pp):
    if len(pp) < 7 or (len(pp) == 7 and 'cid' in pp.keys()):
        return False
    
    x = int(pp['byr'])
    if x < 1920 or x > 2002:
        return False
    
    x = int(pp['iyr'])
    if x < 2010 or x > 2020:
        return False

    x = int(pp['eyr'])
    if x < 2020 or x > 2030:
        return False

    x = pp['ecl']
    if x not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    x = pp['pid']
    if len(x) != 9:
        return False

    # The gross one that made me lookup regex again
    m = re.search(r'(\d+)(\w+)', pp['hgt'])
    x = int(m.group(1))
    if m.group(2) == 'in':
        if x < 59 or x > 76:
            return False
    elif m.group(2) == 'cm':
        if x < 150 or x > 193:
            return False
    else:
        return False
    
    # Forgot hair color, must use regex now :(
    # For future Kat: the hair color must be the pound sign 
    # followed by exactly six hex digits, so that's what the
    # regex matches.
    if not re.match(r'[#](\d|[a-f]){6}', pp['hcl']):
        return False

    # If we passed all conditions
    return True


def part2():
    valid = sum((valid_pp(x) for x in read_passports()))

    print(f'Part 2 answer: {valid}')


if __name__ == '__main__':
    part1()
    part2()
