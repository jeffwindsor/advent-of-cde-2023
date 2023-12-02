def read_input(filename):
    return [line.strip().lower() for line in open(filename,'r').readlines()]

def word_as_digit(s):
    subs = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for k,v in subs.items():
        # padded with initial word before and after since some number "words" shared letters
        # like : ...eigh(t)wo...
        s = s.replace(k, k + v + k)
    return s
    
def score(s):
    digits = [int(c) for c in s if c.isdigit()]
    return (digits[0] * 10) + digits[-1]
    
def part1(filename):
    return sum([score(line) for line in read_input(filename)])
    
def part2(filename):
    return sum([score(word_as_digit(line)) for line in read_input(filename)])
    
print('Part 1e: ', part1('./examples/01_1'))
print('Part 1 : ', part1('./inputs/01'))
print('Part 2e: ', part2('./examples/01_2'))
print('Part 2 : ', part2('./inputs/01'))
