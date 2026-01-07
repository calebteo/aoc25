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
    answer = 0
    
    rules = list(map(lambda x: Rules(int(x.split("-")[0]), int(x.split("-")[1])), content.split("\n\n")[0].split("\n")))

    sort_rules(rules, 0, len(rules) - 1)
    print(rules)

    # Start, count ids, check end and next start. If next start is less than end and smaller than next end -> go from end to next end.
    # start = rules[0].start - 1
    # for i in range(len(rules)):
    #     answer += rules[i].end - start
    #     if (i+1) < len(rules):
    #         if rules[i+1].is_inside_range(rules[i].end):
    #             start = rules[i].end
    #         # case where end is over the other end
    #         elif rules[i].end > rules[i+1].end:
    #             y = i + 2
    #             while y < len(rules):
    #                 if rules[y].is_inside_range(rules[i].end):
    #                     i = y
    #                     start = rules[i].end
    #                     break
    #                 else:
    #                     y += 1
    #         else:
    #             start = rules[i + 1].start - 1

    # # Start, count ids, check end and next start. If next start is less than end and smaller than next end -> go from end to next end.
    # index = 0
    # for i in range(0, rules[-1].end + 1):
    #     print(i)
    #     if rules[index].is_inside_range(i):
    #         answer += 1
    #         print("COUNT" + str(answer))
    #     else: 
    #         if index + 1 < len(rules):
    #             if rules[index + 1].is_inside_range(i):
    #                 index += 1
    #                 answer += 1
    #                 print("COUNT" + str(answer))
    #             else:
    #                 i = rules[index + 1].start
    #                 index += 1

    # Go through each rule. Making a new list of rules. 
    # If the end if larger than the end of next. Move on.
    # If the end is inside the range of the next one. Merge.
    # If the end if less than the start. Start a new one. 
    merged_list = []
    current = 0
    next = current + 1
    new_rule = rules[current]
    merged_list.append(new_rule)
    k = 0
    while next < len(rules):
        current = next
        next = current + 1
        if merged_list[k].end > rules[current].end:
            continue
        elif rules[current].is_inside_range(merged_list[k].end):
            merged_list[k].end = rules[current].end
        elif merged_list[k].end < rules[current].start:
            new_rule = rules[current]
            merged_list.append(new_rule)
            k += 1

    for r in merged_list:
        answer += r.end - r.start + 1

    print(merged_list)
    print(answer)

main()