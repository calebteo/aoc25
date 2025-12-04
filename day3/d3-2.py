import utils.my_utils as utils
import sys

DATA_FILE = utils.get_current_directory(__file__) + "/data/" + "dx.txt"
TEST_FILE = utils.get_current_directory(__file__) + "/data/" + "dx-test.txt"
USE_FILE = DATA_FILE

if len(sys.argv) > 1: 
    mode = sys.argv[1]
    if mode == "test":
        USE_FILE = TEST_FILE

content = utils.read_file(USE_FILE)

def find_next_highest(bank, offset):
    next_highest = 0
    next_highest_index = 0
    for idx, b in enumerate(bank):
        if int(b) > next_highest: 
            next_highest = int(b)
            next_highest_index = idx + offset
        
        if next_highest == 9: 
            break

    return next_highest, next_highest_index
                    

def main():
    answer = 0

    banks = content.split("\n")
    # 2 points. First one finds highest, second finds highest after. 
    for bank in banks:
        print(bank)
        highest = 0
        highest_index = 0
        running_sum = 0
        # do first secparatrely
        highest, highest_index = find_next_highest(bank[:-11], highest_index)
        running_sum += highest * 10**11
        print(running_sum)
        answer += running_sum

        for iteration in range(10,0,-1): 
            highest, highest_index = find_next_highest(bank[highest_index + 1:-iteration], highest_index + 1)
            sum = highest * 10**iteration
            print(sum)
            running_sum += sum
            answer += sum
        
        highest, highest_index = find_next_highest(bank[highest_index + 1:], highest_index + 1)
        print(highest)
        running_sum += highest
        print(running_sum)
        answer += highest
            

    print(f"Answer Part 2: {answer}")
    
main()