from collections import deque
def solution(x, y, n):
    answer = 1000001
    dist = [0 for _ in range(y+1)]
    dq = deque()
    dq.append(x)
    if x== y:
        return 0
    while dq:
        item = dq.popleft()
        for i in range(3):
            if i == 0:
                temp = item * 3
            if i == 1:
                temp = item * 2
            if i == 2:
                temp = item + n
            if temp > y or dist[temp]:
                continue
            if temp == y:
                return dist[item] + 1
            dist[temp] = dist[item] + 1
            dq.append(temp)
        
    return answer if answer != 1000001 else -1