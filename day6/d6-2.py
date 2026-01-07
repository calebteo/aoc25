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

class Column:
    operator: str
    list_of_numbers = []

    def __init__(self):
        self.operator = ""
        self.list_of_numbers = []

    def add_to_list_of_numbers(self, n):
        self.list_of_numbers.append(n)

    def __repr__(self):
        return f"{self.list_of_numbers}" + "Operator: " + self.operator

# Parsing Problem
# Get large denomination by number of rows. 
# Then on every loop lower the denomination for the mutliple factor
# For each n in the line split
# keep a map/list of every digit. 
# Take a string and for each char -> using the denomination -> multiple and add to the sum at that column. (Do condition if not empty.)
# Ideally you still have some way of knowing the largest digit column. Otherwise continue to append to list...?
#

def main():
    answer = 0
    list_of_columns = {}
    parse_operator = False
    for l in content.split("\n"):
        i = 0
        if (l[0] == "*" or l[0] == "+"):
            parse_operator = True
        for n in l.split():
            if not parse_operator:
                if i not in list_of_columns:
                    new_column = Column()
                    new_column.add_to_list_of_numbers(int(n))
                    list_of_columns[i] = new_column
                else:
                    list_of_columns[i].add_to_list_of_numbers(int(n))
            else:
                if i not in list_of_columns:
                    print("Error - should have operator for this index")
                    continue
                else:
                    list_of_columns[i].operator = n
            i += 1

    
    print(list_of_columns)

    for c in list_of_columns.values():
        if c.operator == "*":
            sum = 1
        else:
            sum = 0
        for n in c.list_of_numbers:
            if c.operator == "*":
                sum *= n
            else:
                sum += n

        answer += sum

    print(f"Answer Part 2: {answer}")
    
main()