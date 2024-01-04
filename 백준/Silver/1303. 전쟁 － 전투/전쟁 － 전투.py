from collections import deque
N, M = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
B_list = []
W_list = []
maps = []
visited = [[False for i in range(N)] for _ in range(M)]
for _ in range(M):
    maps.append(list(input()))

def bfs(i: int, j: int):
    types = ''
    if maps[i][j] == 'W':
        types = 'W'
    elif maps[i][j] == 'B':
        types = 'B'
    count = 1
    dq = deque()
    dq.append((i, j))
    visited[i][j] = True
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0 <= ddx < M and 0 <= ddy < N:
                if not visited[ddx][ddy] and maps[ddx][ddy] == maps[x][y]:
                    dq.append((ddx, ddy))
                    visited[ddx][ddy] = True
                    count += 1

    if types == 'W':
        W_list.append(count)
    elif types == 'B':
        B_list.append(count)


for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

w_sum = 0
b_sum = 0
for item in W_list:
    w_sum += item**2

for item in B_list:
    b_sum += item**2

print(w_sum, b_sum)
