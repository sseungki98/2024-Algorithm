from collections import defaultdict
N = int(input())
nodes = list(map(int, input().split()))
answer = 0
node_dict = defaultdict(list)
root = -1
for i in range(N):
    if nodes[i] != -1:
        node_dict[nodes[i]].append(i)
    else:
        root = i

del_node = int(input())


def checkleaf(s_node):
    global answer
    if s_node == del_node:
        return
    elif s_node not in node_dict.keys():

        answer += 1
    else:
        for item in node_dict[s_node]:
            if item != del_node:
                checkleaf(item)
            else:
                if len(node_dict[s_node]) == 1:
                    answer += 1


if root == del_node:
    print(0)

else:
    flag = True
    for root_item in node_dict[root]:
        if root_item != del_node:
            checkleaf(root_item)
            flag = False

    if flag:
        print(1)
    else:
        print(answer)