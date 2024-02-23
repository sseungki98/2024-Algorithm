import sys
from collections import deque
import copy
N, M = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
maps = []
for _ in range(N):
    maps.append(list(map(int, sys.stdin.readline().rstrip())))

answer = []
wall_break = 1

def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    dq = deque()
    dq.append([0, 0, 0])
    visited[0][0][0] = 1
    while dq:
        x, y, z = dq.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][z]
        for k in range(4):
            ddx = x + dx[k]
            ddy = y + dy[k]
            if 0 <= ddx < N and 0 <= ddy < M:
                if maps[ddx][ddy] == 1 and z == 0:
                    visited[ddx][ddy][1] = visited[x][y][z] + 1
                    dq.append([ddx,ddy,1])
                if maps[ddx][ddy] == 0 and visited[ddx][ddy][z] == 0:
                    visited[ddx][ddy][z] = visited[x][y][z] + 1
                    dq.append([ddx, ddy, z])

    return -1


print(bfs())


