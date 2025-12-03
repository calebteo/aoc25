import utils.my_utils as utils
import sys

DATA_FILE = utils.get_current_directory(__file__) + "/data/" + "d2.txt"
TEST_FILE = utils.get_current_directory(__file__) + "/data/" + "d2-test.txt"
USE_FILE = DATA_FILE

if len(sys.argv) > 1: 
    mode = sys.argv[1]
    if mode == "test":
        USE_FILE = TEST_FILE

content = utils.read_file(USE_FILE)

def find_invalid_ids_at_least_two(range_ids: str):
    sum = 0

    range_start = int(range_ids.split("-")[0])
    range_end = int(range_ids.split("-")[1]) + 1
    
    # Go over ranges
    # Sliding window. Start at 1, 2 ... including len/2
    for i in range(range_start, range_end):
        # Window
        window_for_i = len(str(i))
        id = str(i)
        for window_size in range(1, window_for_i // 2 + 1):
            first_pattern = id[0:window_size]
            next_window = 1
            invalid_id = True
            while(next_window*window_size < window_for_i):
                next_pattern = id[next_window*window_size:next_window*window_size + window_size]
                if first_pattern != next_pattern:
                    invalid_id = False
                    break
                next_window += 1
            
            if invalid_id:
                sum += i
                break
        
    return sum
                    

def main():
    answer = 0
    print(content) 
    
    ranges = content.split(",")

    for r in ranges: 
        answer += find_invalid_ids_at_least_two(r)


    print(f"Answer Part 2: {answer}")
    
main()