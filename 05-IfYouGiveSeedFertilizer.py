from functools import reduce

def is_seed_in_range(rangeStart, rangeLength, seed):
	return (seed - rangeStart) >= 0 and (seed - rangeStart) < rangeLength 

def map_seed(seed, planting_map):
	for destinationStart, sourceStart, length in planting_map:
		if is_seed_in_range(sourceStart, length, seed):
			return destinationStart + (seed - sourceStart)
	#return input if no seed is in range of any planting_map
	return seed
	
def answer_part_1(seeds, planting_maps):
	return min([reduce(map_seed, planting_maps, seed) for seed in seeds])







def split_into_tuples(xs, chunk_size):
	for i in range(0, len(xs), chunk_size):
		yield tuple(xs[i:i + chunk_size])

def answer_part_2(seeds, maps):
	return list(split_into_tuples(seeds, 2))


##################################################################
def test_is_seed_in_range_within1(): assert is_seed_in_range(0,5,4) == True
def test_is_seed_in_range_within2(): assert is_seed_in_range(0,5,0) == True
def test_is_seed_in_range_after(): assert is_seed_in_range(0,5,5) == False
def test_is_seed_in_range_before(): assert is_seed_in_range(1,5,0) == False

def test_map_seed():
	assert map_seed(79,[(52, 50, 48)]) == 81
	
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
	print('Part 2e:', answer_part_2(*example1))
	# print('Part 2 :', answer_part_2(input))

	
if __name__ == "__main__":
	main()
