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
    print("Answer Part 1:")
    
main()