from itertools import combinations
from collections import deque
N, M = map(int, input().split())
move_dict = {}
for _ in range(N+M):
    move_info = (list(map(int, input().split())))
    move_dict[move_info[0]] = move_info[1]


def bfs():
    position = 1
    dq = deque()
    visited = [[False, 0] for _ in range(101)]
    visited[position][0] = True
    visited[position][1] = 1
    dq.append([position, 0])
    while dq:
        x, move_count = dq.popleft()
        move_count += 1
        for i in range(6):
            nx = x + i + 1
            if nx > 100:
                continue
            if visited[nx][0] and visited[nx][1] < move_count:
                continue
            if nx == 100:
                return move_count
            if nx < 100:
                if nx in move_dict.keys():
                    nx = move_dict[nx]

            dq.append([nx, move_count])
            visited[nx][0] = True
            visited[nx][1] = move_count

    return visited[100][1]

print(bfs())



