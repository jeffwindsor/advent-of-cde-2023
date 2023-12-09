from functools import reduce 
import operator

# def find_optimal_charge_time(distance, time_limit, base_speed=0):
#     low, high = 0, time_limit
    
#     while low <= high:
#         mid = (low + high) // 2
#         race_time = calculate_race_time(distance, mid, base_speed)
        
#         if race_time <= time_limit:
#             # Feasible, move towards lower charging time
#             high = mid - 1
#         else:
#             # Not feasible, need more charging time
#             low = mid + 1
    
#     # The optimal charge time is likely in the low or mid variable
#     return low

def winning_distances(race_with_charge_times):
    for charge_time, race_time, distance_to_beat in race_with_charge_times:
        race_distance = (race_time - charge_time) * charge_time
        if race_distance > distance_to_beat:
            yield race_distance

def add_possible_charge_times(rt,rd): 
    # both charge time of 0 and charge time = race time results in zero, so left them out
    return [(ct, rt, rd) for ct in range(1, rt)]
    
def expand_with_charge_times(races):
    return [add_possible_charge_times(race_time, record_distance)
            for race_time, record_distance in list(races)]

# race = (time, distance)
def answer_part_1(races):
    count_of_winning_charge_times = [len(list(winning_distances(race_with_charge_time))) 
                                     for race_with_charge_time in expand_with_charge_times(races)]
    return reduce(operator.mul, count_of_winning_charge_times, 1)

def answer_part_2(race):
    return len(list(winning_distances(add_possible_charge_times(*race))))
    
##################################################################

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
    print('Part 2e:', answer_part_2(parse_input_as_single_value('data/06_01e')))
    print('Part 2 :', answer_part_2(parse_input_as_single_value('data/06')))

if __name__ == "__main__":
	main()
