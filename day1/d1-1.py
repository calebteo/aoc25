import utils.my_utils as utils
import sys

DATA_FILE = utils.get_current_directory(__file__) + "/data/" + "d1.txt"
TEST_FILE = utils.get_current_directory(__file__) + "/data/" + "d1-test.txt"
USE_FILE = DATA_FILE

if len(sys.argv) > 1: 
    mode = sys.argv[1]
    if mode == "test":
        USE_FILE = TEST_FILE

content = utils.read_file(USE_FILE)

def main():
    current = 50
    counter = 0

    for line in content.split("\n"):
        direction = line[0]
        clicks = int(line[1:4])
        if clicks > 100:
            clicks = clicks%100
            
        if direction == "R": # Turning Right means postive
            current += clicks
        else:
            current -= clicks

        if current >= 100: 
            current -= 100
        elif current < 0: 
            current += 100

        if current == 0:
            counter += 1


    print ("Answer:" + str(counter))
    
main()