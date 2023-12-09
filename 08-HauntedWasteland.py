import parse
from math import lcm
from itertools import cycle

def parse_input(filename):
    lines = [*open(filename)]
    path = lines[0].strip()
    instructions = {}
    for line in lines[2:]:
        node, l, r = parse.parse("{:w} = ({:w}, {:w})", line.strip())
        instructions[node] = {'L':l, 'R':r}
    return path, instructions

def find_path(instructions, nodes, current, is_end):
	moves = 0
	for move in cycle(instructions):
		current = nodes[current][move]
		moves += 1
		if is_end(current): return moves
		
def answer_part_1(instructions, nodes):
	return find_path(instructions,nodes,'AAA', lambda s: s == 'ZZZ')
	
def answer_part_2(instructions, nodes):
	starts = (key for key in nodes.keys() if key.endswith('Z'))
	paths = (find_path(instructions,nodes,start, lambda s: s.endswith('Z')) for start in starts)
	return lcm(*paths)
	
print(answer_part_1(*parse_input('data/08_02e')))
print(answer_part_1(*parse_input('data/08')))
print(answer_part_2(*parse_input('data/08_03e')))
print(answer_part_2(*parse_input('data/08')))
