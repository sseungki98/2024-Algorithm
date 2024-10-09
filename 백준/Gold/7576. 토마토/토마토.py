from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
tomatoes = []
for _ in range(M):
    tomatoes.append(list(map(int, input().split())))

# 1 : 익은, 0 : 익지 않은, -1 : 토마토가 없는

visited = [[False for _ in range(N)] for _ in range(M)]
def bfs(tomato_start):
    dq = []
    for item in tomato_start:
        dq.append(item)
    for item in dq:
        visited[item[0]][item[1]] = True
    temp_store = []
    count = 0
    while dq:
        temp_dq = deque(dq)

        while temp_dq:
            x, y = temp_dq.popleft()
            for i in range(4):
                ddx = x + dx[i]
                ddy = y + dy[i]
                if 0 <= ddx < M and 0 <= ddy < N:
                    if tomatoes[ddx][ddy] == 0 and visited[ddx][ddy] == False:
                        temp_store.append([ddx, ddy])
                        tomatoes[ddx][ddy] = 1
                        # visited[ddx][ddy] = True
        dq = temp_store
        temp_store = []
        count += 1

    return count
tomato = []
for i in range(M):
    for j in range(N):
        if tomatoes[i][j] == 1:
            tomato.append([i, j])

ans = (bfs(tomato))

for i in range(M):
    for j in range(N):
        if tomatoes[i][j] == 0:
            print(-1)
            exit()

print(ans-1)
