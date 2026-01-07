import utils.my_utils as utils
import sys
import math

DATA_FILE = utils.get_current_directory(__file__) + "/data/" + "dx.txt"
TEST_FILE = utils.get_current_directory(__file__) + "/data/" + "dx-test.txt"
USE_FILE = DATA_FILE

if len(sys.argv) > 1: 
    mode = sys.argv[1]
    if mode == "test":
        USE_FILE = TEST_FILE

content = utils.read_file(USE_FILE)

class Rules():
    start: int
    end: int
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return str(self.start) + " - " + str(self.end)
    
    def is_inside_range(self, n): 
        return n >= self.start and n <= self.end
    

def sort_rules(rules, left, right):
    
    def sort_unit(rules, left, mid, right):
        i = 0
        j = 0
        k = left
        left_rules = rules[left : mid + 1]
        right_rules = rules[mid + 1 : right + 1]
        left_size = len(left_rules)
        right_size = len(right_rules)
        
        while (i < left_size and j < right_size): 
            if left_rules[i].start >= right_rules[j].start:
                rules[k] = right_rules[j]
                j += 1
            else:
                rules[k] = left_rules[i]
                i += 1

            k += 1
        
        if i < left_size: 
            # Add remain left
            for remain in left_rules[i:left_size]:
                rules[k] = remain
                k += 1

        if j < right_size:
            # Add remaining right
            for remain in right_rules[j:right_size]:
                rules[k] = remain
                k += 1
    
    if left < right:
        mid = (left + right) // 2

        sort_rules(rules, left, mid)
        sort_rules(rules, mid + 1, right)
        sort_unit(rules, left, mid, right)
    

def main():
    rules = []
    numbers = []
    answer = 0
    
    rules = list(map(lambda x: Rules(int(x.split("-")[0]), int(x.split("-")[1])), content.split("\n\n")[0].split("\n")))
    numbers = list(map(lambda x:int(x), content.split("\n\n")[1].split("\n")))
    print(numbers)

    sort_rules(rules, 0, len(rules) - 1)
    print(rules)

    # for n in numbers:
    #     start = 0
    #     end = len(rules) - 1
    #     mid = (end + start) // 2
    #     while start <= end: 
    #         if rules[mid].is_inside_range(n):
    #             answer += 1
    #             break
    #         else:
    #             if n > rules[mid].start: 
    #                 start = mid + 1
    #                 mid = (end + start) // 2
    #             else:
    #                 end = mid - 1
    #                 mid = (end + start) // 2

    # print(f"Answer Part 1: {answer}")

    brute=0
    for n in numbers:
        for r in rules:
            if r.is_inside_range(n):
                brute += 1
                break

    print(brute)
    
    
main()