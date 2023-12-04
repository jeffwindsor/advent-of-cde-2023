import parse
from functools import reduce

def color_max_counts(ccs):
	result = {'red':0, 'blue':0, 'green':0}
	for cc in ccs:
		for (color,count) in cc:
			color_count = result[color]
			if count > result[color]:
				result[color] = count
	return result

def is_game_possible(game_result):
	cubes = {'red':12, 'blue':14, 'green':13}
	cps = [ game_result[cube_color] <= cube_count 
			for cube_color, cube_count in cubes.items()]
	return sum(cps) == 3

def answer1(inputs):
	return sum([input['id'] 
	           	for input in inputs 
	           	if is_game_possible(color_max_counts(input['subsets']))])

def answer2(inputs):
	def score(color_counts):
		 return reduce(lambda a,b: a * b, color_counts.values())
	return sum([score(color_max_counts(input['subsets'])) for input in inputs])	

##################################################################
def parse_as_int(s):
	return int(s)

def parse_as_subsets(s):
	return [parse_as_subset(subset) for subset in s.split('; ')]

def parse_as_subset(s):
	return [parse_as_color_count(cc) for cc in s.split(', ')]

def parse_as_color_count(s):
	ss = s.split(' ')
	return (ss[1], parse_as_int(ss[0]))
	
def parse_input(filename):
	# pre-compile parsers since used more than once
	line_parser = parse.compile("Game {id:integer}: {subsets:subsetList}", {"integer": parse_as_int, "subsetList": parse_as_subsets})
	# parse each line
	return [ line_parser.parse(line.strip()).named for line in open(filename,'r').readlines() ]

##################################################################
def main():
	example1 = parse_input('data/02_1e')	
	example2 = parse_input('data/02_2e')	
	input    = parse_input('data/02')	
	print('Part 1e: ', answer1(example1))
	print('Part 1:  ', answer1(input))
	print('Part 2e: ', answer2(example2))
	print('Part 2:  ', answer2(input))

	
if __name__ == "__main__":
    main()
