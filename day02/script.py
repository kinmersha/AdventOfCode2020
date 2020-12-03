import math

class Password:
    def __init__(self, pMin, pMax, pChar, text):
        self.pMin = pMin # Minimum occurences of pChar to be valid for the policy
        self.pMax = pMax # Maximum " "
        self.pChar = pChar # The character that must appear to be valid
        self.text = text # The text of the password
    
    def isValid(self):
        if self.pMin <= self.text.count(self.pChar) <= self.pMax:
            return True
        else:
            return False

    @staticmethod
    def createPassword(line):
        tokens = line.split()
        # tokens[0] = policy count in the form `n-m`
        pMin, pMax = (int(x) for x in tokens[0].split('-')) # be smrt
        # tokens[1] = policy required character x in the format `x:`
        pChar = tokens[1].strip(':')
        # tokens[2] = the password in plaintext
        text = tokens[2]

        return Password(pMin, pMax, pChar, text)


def read_data():
    with open('day02/input') as f:
        passwords = []
        for line in f:
            passwords.append(Password.createPassword(line))
    return passwords

def part1():
    passwords = read_data()
    tf = [p.isValid() for p in passwords]
    print(f'Part 1 answer: {sum(tf)}')



if __name__ == '__main__':
    part1()
    # part2()