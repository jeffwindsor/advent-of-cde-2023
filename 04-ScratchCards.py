import parse

def matches(winners, numbers):
    return len(set(winners).intersection(set(numbers)))

def score(matches):
    return (2 ** (matches - 1)) if matches > 0 else 0

def answer_part_1(cards):
    return sum([score(matches(c['winners'], c['numbers'])) for c in cards])

# assumes that card input is in order
def answer_part_2(cards):
    card_counts_by_id = dict([(c['id'], 1) for c in cards])
    id_matches = [(c['id'], matches(c['winners'], c['numbers'])) for c in cards]
    for card_id, card_matches in id_matches:
        for new_card_id in range(card_id + 1, card_id + 1 + card_matches):
            # add winnings to card counts
            card_counts_by_id[new_card_id] = card_counts_by_id[new_card_id] + card_counts_by_id[card_id]    
    return sum([count for id, count in card_counts_by_id.items()])
    
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
    print('Part 2e:', answer_part_2(example1))
    print('Part 2 :', answer_part_2(input))

	
if __name__ == "__main__":
    main()
