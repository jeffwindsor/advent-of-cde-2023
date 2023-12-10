from functools import reduce 
import operator
import math

def wins(race_time, distance_record):
    is_win = lambda ct: ((race_time - ct) * ct) > distance_record
    return sum((is_win(charge_time) for charge_time in range(1, race_time)))

def answer_part_1(races):
    race_wins = [wins(race_time, distance_record) for race_time, distance_record in races]
    return reduce(operator.mul, race_wins, 1)

def quadratic(race_time, distanace_record):
    a = math.ceil((race_time - math.sqrt(race_time**2 - 4 * distanace_record))/2)
    b = math.floor((race_time + math.sqrt(race_time**2 - 4 * distanace_record))/2)
    return (a,b)

def answer_part_2(race_time, distance_to_beat):
    a,b = quadratic(race_time, distance_to_beat)
    return (b - a) + 1
    
##################################################################
def test_quadratic():
    assert quadratic(71530, 940200) == (14, 71516)
    
##################################################################
def parse_input_as_list(filename):
    # combine the time and distance lines into pairs
    lines = [line.strip()[9:].split() for line in open(filename,'r').readlines()]
    # turn inputs values into integers
    return zip(map(int,lines[0]), map(int,lines[1]))

def parse_input_as_single_value(filename):
    # combine the time and distance lines into pairs
    lines = [line.strip()[9:].replace(' ','') for line in open(filename,'r').readlines()]
    # turn inputs values into integers
    return tuple(map(int, lines)
)
##################################################################
def main():
    # print(parse_input_as_single_value('data/06_01e'))
    print('Part 1e:', answer_part_1(parse_input_as_list('data/06_01e')))
    print('Part 1 :', answer_part_1(parse_input_as_list('data/06')))
    print('Part 2e:', answer_part_2(*parse_input_as_single_value('data/06_01e')))
    print('Part 2 :', answer_part_2(*parse_input_as_single_value('data/06')))

if __name__ == "__main__":
	main()
