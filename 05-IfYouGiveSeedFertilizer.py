from functools import reduce

def in_range(start, length, value):
	return (value - start) >= 0 and (value - start) < length 

def apply_map(value, map):
	for destinationStart, sourceStart, length in map:
		if in_range(sourceStart, length, value):
			return destinationStart + (value - sourceStart)
	#return input if no value is in range of any map
	return value
	
def seed2location(seed, maps):
	return reduce(apply_map, maps, seed)
	
def answer_part_1(seeds, maps):
	return min([seed2location(seed, maps) for seed in seeds])

def split_into_tuples(xs, chunk_size):
	for i in range(0, len(xs), chunk_size):
		yield tuple(xs[i:i + chunk_size])

def answer_part_2(seeds, maps):
	pass

##################################################################
def test_in_range_within1(): assert in_range(0,5,4) == True
def test_in_range_within2(): assert in_range(0,5,0) == True
def test_in_range_after(): assert in_range(0,5,5) == False
def test_in_range_before(): assert in_range(1,5,0) == False

def test_app_map_example():
	assert apply_map(79,[(52, 50, 48)]) == 81
	
def test_seed2location_given_no_matches_then_original_input():
	maps = [[(1,0,5)],[(10,0,5)]]
	assert seed2location(7, maps) == 7

def test_split_into_tuples_seeds_as_pairs():
	seeds = [79, 14, 55, 13]
	assert list(split_into_tuples(seeds, 2)) == [(79, 14), (55, 13)]
	
##################################################################
def parse_as_map(s):
	rows = s.split('\n')[1:]
	return [ tuple(parse_as_int_list(r)) for r in rows]
	
def parse_as_int_list(s):
	return [int(i) for i in s.split(' ')]
	
def parse_input(filename):
	chunks = [line.strip() 
		for line in open(filename,'r').read().split('\n\n') 
		if line != '\n']
	seeds = parse_as_int_list(chunks[0].replace('seeds: ',''))
	maps = [parse_as_map(c) for c in chunks[1:]]
	return seeds, maps

##################################################################
def main():
	example1 = parse_input('data/05_1e')
	# print(example1)
	input = parse_input('data/05')
	print('Part 1e:', answer_part_1(*example1))
	print('Part 1 :', answer_part_1(*input))
	# print('Part 2e:', answer_part_2(example1))
	# print('Part 2 :', answer_part_2(input))

	
if __name__ == "__main__":
	main()
