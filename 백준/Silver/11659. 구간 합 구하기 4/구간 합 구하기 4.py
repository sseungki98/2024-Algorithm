N, M = map(int, input().split())
stack = list(map(int, input().split()))

s_e_list = []
sum_list = [0]
for _ in range(M):
    s_e_list.append(list(map(int, input().split())))
    
sum = 0
for i in range(len(stack)):
    sum += stack[i]
    sum_list.append(sum)

for item in s_e_list:
    start, end = item[0], item[1]

    print(sum_list[end] - sum_list[start-1])
