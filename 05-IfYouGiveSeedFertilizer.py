from functools import reduce
from enum import Enum

def is_seed_in_range(rangeStart, rangeLength, seed):
	return (seed - rangeStart) >= 0 and (seed - rangeStart) < rangeLength 

def map_seed(seed, planting_map):
	for destinationStart, sourceStart, length in planting_map:
		if is_seed_in_range(sourceStart, length, seed):
			return destinationStart + (seed - sourceStart)
	#return input if no seed is in range of any planting map range
	return seed
	
def answer_part_1(seeds, planting_maps):
	# apply seed to each planing map in order, take minimum result
	apply_planting_maps = lambda seed: reduce(map_seed, planting_maps, seed) 
	return min([apply_planting_maps(seed) for seed in seeds])

Overlap = Enum('Overlap', ['TOTAL', 'TOP', 'BOTTOM', 'INSIDE', 'WRAPS', 'NONE'])

def get_overlap(aStart,aEnd,bStart,bEnd):
	if aStart == bStart and aEnd == bEnd:
		return Overlap.TOTAL
	elif aStart < bStart and bStart < aEnd and aEnd < bEnd:
		return Overlap.BOTTOM
	elif aStart > bStart and aStart < bEnd and aEnd > bEnd:
		return Overlap.TOP
	elif bStart < aStart and aEnd < bEnd:
		return Overlap.INSIDE
	elif aStart < bStart and bEnd < aEnd:
		return Overlap.WRAPS
	return Overlap.NONE

def merge_ranges(ranges):
	# should sort and merge any overlapping ranges
	return ranges

def get_overlaps(seedStart, seedLength, sourceStart, mapLength, destinationStart):
	seedEnd = seedStart + seedLength - 1
	sourceEnd = sourceStart + mapLength - 1
	match get_overlap(seedStart, seedEnd, sourceStart, sourceEnd):
		case Overlap.TOTAL:
			return [(destinationStart, mapLength)]
		case Overlap.BOTTOM:
			nonOverlapLength = sourceStart - seedStart
			return merge_ranges([(seedStart, nonOverlapLength), (destinationStart, seedLength - nonOverlapLength)])
		case Overlap.TOP: 
			overlapLength = sourceEnd - seedStart
			return merge_ranges([(seedStart, seedLength - overlapLength),(destinationStart, overlapLength)])

	# Overlap NONE
	return [(seedStart,seedLength)]

# using seed ranges here for recursion
def map_seed_range(seedRanges, planting_map):
	return [get_overlaps(seedStart, seedLength,sourceStart,mapLength,destinationStart) 
		for destinationStart, sourceStart, mapLength in planting_map
		for seedStart, seedLength in seedRanges
	]

def split_into_tuples(xs, chunk_size):
	for i in range(0, len(xs), chunk_size):
		yield tuple(xs[i:i + chunk_size])

def answer_part_2(seeds, planting_maps):
	seedRanges = split_into_tuples(seeds, 2)
	apply_planting_maps = lambda seedRange: reduce(map_seed_range, planting_maps, [seedRange])
	return [apply_planting_maps(seedRange) for seedRange in seedRanges]


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
	
def test_get_overlaps_given_no_overlap_then_original_seed_range():
	assert get_overlaps(0,7,10,7,20) == [(0,7)]  

def test_get_overlaps_given_full_overlap_then_destination_range():
	assert get_overlaps(0,7,0,7,20) == [(20,7)]  

def test_get_overlaps_given_overlap_with_bottom_of_seed_then_2split_bottom_conversion():
	assert get_overlaps(10,11,15,1000,100) == [(10, 5), (100, 6)]  

def test_get_overlaps_given_overlap_with_top_of_seed_then_2split_top_conversion():
	assert get_overlaps(15,1000,10,11,100) == [(15,995), (100, 5)]  

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
	# print('Part 2e:', answer_part_2(*example1))
	# print('Part 2 :', answer_part_2(input))

	
if __name__ == "__main__":
	main()
