import parse

def score(winners, numbers):
    count = len(set(winners).intersection(set(numbers)))
    return (2 ** (count - 1)) if count > 0 else 0

def answer_part_1(cards):
    return sum([score(c['winners'], c['numbers']) for c in cards])
    
##################################################################
def parse_as_int(s):
	return int(s)

def parse_as_int_list(s):
	return [int(n) for n in s.strip().split(' ') if n.isdigit()]

def parse_input(filename):
	line_parser = parse.compile("Card {id:cardId}: {winners:cardNumbers} | {numbers:cardNumbers}", 
	                            {"cardId": parse_as_int, "cardNumbers": parse_as_int_list})
	return [ line_parser.parse(line.strip()).named for line in open(filename,'r').readlines() ]

##################################################################
def main():
    example1 = parse_input('data/04_1e')	
    input = parse_input('data/04')
    print('Part 1e:', answer_part_1(example1))
    print('Part 1 :', answer_part_1(input))

	
if __name__ == "__main__":
    main()
