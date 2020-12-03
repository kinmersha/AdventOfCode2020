import math
from abc import abstractmethod

class Password:
    def __init__(self, pMin, pMax, pChar, text):
        self.pMin = pMin # Minimum occurences of pChar to be valid for the policy
        self.pMax = pMax # Maximum " "
        self.pChar = pChar # The character that must appear to be valid
        self.text = text # The text of the password
    
    @abstractmethod
    def isValid(self):
        pass
    
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

class Part1Password(Password):
    # Expects to be given a Password object
    def __init__(self, pword):
        self.pMin = pword.pMin
        self.pMax = pword.pMax
        self.pChar = pword.pChar
        self.text = pword.text

    def isValid(self):
        if self.pMin <= self.text.count(self.pChar) <= self.pMax:
            return True
        else:
            return False


class Part2Password(Password):
    # Expects to be given a Password object
    def __init__(self, pword):
        self.pMin = pword.pMin - 1 # New certification gives indices in base-1
        self.pMax = pword.pMax - 1 # ditto
        self.pChar = pword.pChar
        self.text = pword.text

    def isValid(self):
        if (self.text[self.pMin] == self.pChar) ^ (self.text[self.pMax] == self.pChar):
            return True
        else:
            return False



def read_data():
    with open('day02/input') as f:
        passwords = []
        for line in f:
            passwords.append(Password.createPassword(line))
    return passwords

def part1():
    passwords = [Part1Password(p) for p in read_data()]
    tf = [p.isValid() for p in passwords]
    print(f'Part 1 answer: {sum(tf)}')

def part2():
    passwords = [Part2Password(p) for p in read_data()]
    tf = [p.isValid() for p in passwords]
    print(f'Part 1 answer: {sum(tf)}')



if __name__ == '__main__':
    part1()
    part2()
