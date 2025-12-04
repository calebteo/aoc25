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

def main():
    answer = 0

    banks = content.split("\n")
    # 2 points. First one finds highest, second finds highest after. 
    for bank in banks:
        print(bank)
        highest = 0
        highest_index = 0
        second = 0
        second_index = 0
        for idx, b in enumerate(bank[:-1]):
            if int(b) > highest: 
                highest = int(b)
                highest_index = idx
            
            if highest == 9: 
                 break
                 
        
        for idx, b in enumerate(bank[highest_index + 1:]):
            if int(b) > second: 
                second = int(b)
                second_index = idx
            
            if second == 9: 
                 break
            
        # if second_index < highest_index:
        #     print("flipping")
        #     highest, second = second, highest

        sum = highest * 10 + second
        print(sum)

        answer += sum
            

    print(f"Answer Part 1: {answer}")
    
main()