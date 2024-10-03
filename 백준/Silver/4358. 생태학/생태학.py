from collections import defaultdict
import sys

tree_dict = defaultdict(int)

while True:
    info = sys.stdin.readline().rstrip()
    if info == "":
        break
    tree_dict[info] += 1


answer_list = []

total_tree_num = sum(tree_dict.values())

for key, value in tree_dict.items():
    answer_list.append([key, value / total_tree_num * 100])

answer_list = sorted(answer_list, key = lambda x:x[0])

for item in answer_list:
    print('%s %.4f' %(item[0], item[1]))
