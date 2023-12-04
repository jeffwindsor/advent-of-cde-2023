import re
from dataclasses import dataclass
from functools import partial, reduce

# COORD SHAPE: (row, colStart, colEnd, value)
def get_pattern(pattern, engine_schematic):
  return [(row, match.start(), match.end(), match.group()) 
          for row, line in enumerate(engine_schematic)
          for match in re.finditer(pattern, line) if type(match) is re.Match]            

# any char that is not a '.' or a digit
get_symbols = partial(get_pattern, r'[^(\d)|^(\.)]')

# any contiguous sequence of digits
get_numbers = partial(get_pattern, r'\d+')

def surrounding_points(coord):
  row,colStart,colEnd,value = coord
  above  = [(row - 1, col) for col in range(colStart - 1, colEnd + 1)]
  on_row = [(row,colStart - 1),(row, colEnd)]
  below  = [(row + 1, col) for col in range(colStart - 1, colEnd + 1)]
  return above + on_row + below

def internal_points(coord):
  row,colStart,colEnd,value = coord
  return [(row, col) for col in range(colStart,colEnd)]
    
def number_as_int(number):
  return int(number[3])
  
def answer_part_1(engine_schematic):
  def is_next_to_symbol(number, symbol_points):
    #short cutting true just in case
    for p in surrounding_points(number):
      if p in symbol_points:
        return True
    return False

  symbol_points = set([ (symbol[0], symbol[1]) for symbol in get_symbols(engine_schematic)])
  numbers = get_numbers(engine_schematic)
  part_numbers = [number_as_int(number) 
                  for number in numbers 
                  if is_next_to_symbol(number,symbol_points)]
  return sum(part_numbers)

def answer_part_2(engine_schematic):
  def adjacent_numbers_to_symbol(symbol, numbers_by_digit_points):
    # use set to remove any duplicate number coordinates (the value in the dictionary)
    return list(set([numbers_by_digit_points[sp] 
                for sp in surrounding_points(symbol) 
                if sp in numbers_by_digit_points]))

  def score_for_gear(numbers):
    return reduce(lambda a,b: a * b, [number_as_int(n) for n in numbers])
  
  numbers_by_digit_points = dict([ (number_point, number)
                         for number in get_numbers(engine_schematic)
                         for number_point in internal_points(number)])
  stars = [symbol for symbol in get_symbols(engine_schematic) if symbol[3] == '*']
  possibles = [adjacent_numbers_to_symbol(s, numbers_by_digit_points) for s in stars]
  gears = [score_for_gear(ps) for ps in possibles if len(ps) == 2]
  return sum(gears)

####################################################################
def test_symbols_empty(): assert get_symbols(['....', '....', '....']) == []
def test_symbols_1(): assert get_symbols(['...!..58.']) == [(0,3,4,'!')]
def test_symbols_2(): assert get_symbols(['...@..58.']) == [(0,3,4,'@')]
def test_symbols_3(): assert get_symbols(['...#..58.']) == [(0,3,4,'#')]
def test_symbols_4(): assert get_symbols(['...$..58.']) == [(0,3,4,'$')]
def test_symbols_5(): assert get_symbols(['...%..58.']) == [(0,3,4,'%')]
def test_symbols_6(): assert get_symbols(['.../..58.']) == [(0,3,4,'/')]
def test_symbols_7(): assert get_symbols(['...&..58.']) == [(0,3,4,'&')]
def test_symbols_8(): assert get_symbols(['...*..58.']) == [(0,3,4,'*')]
def test_symbols_9(): assert get_symbols(['...+..58.']) == [(0,3,4,'+')]
def test_symbols_10(): assert get_symbols(['...-..58.']) == [(0,3,4,'-')]
def test_symbols_11(): assert get_symbols(['...=..58.']) == [(0,3,4,'=')]
  
def test_numbers_empty(): assert get_numbers(['....', '....', '....']) == []
def test_numbers():  assert get_numbers(['..........', '..123..56.', '..........']) == [(1,2,5,'123'),(1,7,9,'56')]

def test_surrounding_points():
  assert set(surrounding_points((1,5,8,'114'))) == set([(0,4), (0,5), (0,6), (0,7), (0,8), (1,4), (1,8), (2,4), (2,5), (2,6), (2,7), (2,8)])

def test_internal_points():
  assert set(internal_points((1,5,8,'114'))) == set([(1,5),(1,6),(1,7)])

####################################################################
def read_engine_schematic(filename):
 return [ line.strip() for line in open(filename,'r').readlines() ]

####################################################################
def main():
  example = read_engine_schematic('./data/03_1e')
  inputs  = read_engine_schematic('./data/03')
  print('Part 1e:', answer_part_1(example))
  print('Part 1 :', answer_part_1(inputs))
  print('Part 2e:', answer_part_2(example))
  print('Part 2 :', answer_part_2(inputs))

if __name__ == "__main__":
    main()
    
