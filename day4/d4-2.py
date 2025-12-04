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

directions = [(1,0),(0,1),(1,1),(-1,0),(0,-1),(1,-1),(-1,1), (-1,-1)]

def read_in_as_2d_array(content: str):
    my_array = []
    for l in content.split("\n"):
        row = []
        for c in l:
            row.append(c)
        my_array.append(row)

    return my_array

def check_surroundings(x, y, map, MAX_X, MAX_Y):
    count_sides = 0
    for d in directions:
        check_x = x + d[0]
        check_y = y + d[1]
        if check_x >= 0 and check_x < MAX_X:
            if check_y >= 0 and check_y < MAX_Y:
                if map[check_y][check_x] == "@":
                    count_sides += 1
    
    if count_sides < 4:
        return True
    else: 
        return False

def main():
    answer = 0

    my_map = read_in_as_2d_array(content)
    print(my_map)
    MAX_Y = len(my_map)
    MAX_X = len(my_map[0])
    print(MAX_X)
    print(MAX_Y)

    current_iteration_counter = 0
    iteration = 0
    to_remove = []

    for y in range(0, MAX_Y):
        for x in range(0, MAX_Y):
            if my_map[y][x] == "@":
                isClear = check_surroundings(x, y, my_map, MAX_X, MAX_Y)
                if isClear:
                    current_iteration_counter += 1
                    # Replace @ with x
                    to_remove.append((x,y))
                    
    print(str(iteration) + ":" + "Removed " + str(current_iteration_counter))
    answer += current_iteration_counter

    for r in to_remove:
        my_map[r[1]][r[0]] = "x"

    while current_iteration_counter != 0:
        current_iteration_counter = 0
        iteration += 1
        to_remove = []
        for y in range(0, MAX_Y):
            for x in range(0, MAX_Y):
                if my_map[y][x] == "@":
                    isClear = check_surroundings(x, y, my_map, MAX_X, MAX_Y)
                    if isClear:
                        current_iteration_counter += 1
                        to_remove.append((x,y))
        
        print(str(iteration) + ":" + "Removed " + str(current_iteration_counter))
        answer += current_iteration_counter

        for r in to_remove:
            my_map[r[1]][r[0]] = "x"


    print(f"Answer Part 2: {answer}")
    
main()