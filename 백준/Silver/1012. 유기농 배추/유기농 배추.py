from collections import deque
T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(start_x, start_y, route):
    dq = deque()
    route[start_x][start_y] = 0
    dq.append([start_x, start_y])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx < 0 or ddx >= M or ddy < 0 or ddy >= N:
                continue
            else:
                if route[ddx][ddy] == 1:
                    dq.append([ddx, ddy])
                    route[ddx][ddy] = 0


for _ in range(T):
    M, N, K = map(int, input().split())
    total_count = 0
    maps = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        maps[x][y] = 1

    for i in range(M):
        for j in range(N):
            if maps[i][j] == 1:
                bfs(i,j,maps)
                total_count += 1

    print(total_count)






