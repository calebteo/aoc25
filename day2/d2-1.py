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

def find_invalid_ids(range_ids: str):
    sum = 0

    range_start = int(range_ids.split("-")[0])
    range_end = int(range_ids.split("-")[1]) + 1

    # Go over range
    for i in range(range_start, range_end):
        if len(str(i)) % 2 == 0:
            first = str(i)[0:len(str(i))//2]
            second = str(i)[len(str(i))//2:len(str(i))]
            if first == second:
                sum += i
    
    return sum

def main():
    answer = 0

    # Read in
    print(content) 
    
    ranges = content.split(",")

    for r in ranges: 
        answer += find_invalid_ids(r)


    print(f"Answer Part 1: {answer}")
    
main()