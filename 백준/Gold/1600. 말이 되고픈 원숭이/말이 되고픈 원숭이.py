from collections import deque

K = int(input())
W, H = map(int, input().split())
maps = []
for _ in range(H):
    maps.append(list(map(int, input().split())))

horse_move_x = [2, 2, 1, 1, -2, -2, -1, -1]
horse_move_y = [1, -1, 2, -2, 1, -1, 2, -2]
move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]
visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]

def bfs():
    dq = deque()
    dq.append([0, 0, K])
    while dq:
        x, y, left_horse_move = dq.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][left_horse_move]
        if left_horse_move > 0:
            for i in range(8):
                dx = x + horse_move_x[i]
                dy = y + horse_move_y[i]
                if 0 <= dx < H and 0 <= dy < W:
                    if maps[dx][dy] == 0 and visited[dx][dy][left_horse_move-1] == 0:
                         visited[dx][dy][left_horse_move-1] = visited[x][y][left_horse_move] + 1
                         dq.append([dx, dy, left_horse_move-1])

        for i in range(4):
            dx = x + move_x[i]
            dy = y + move_y[i]
            if 0 <= dx < H and 0 <= dy < W:
                if maps[dx][dy] == 0 and visited[dx][dy][left_horse_move] == 0:
                    visited[dx][dy][left_horse_move] = visited[x][y][left_horse_move] + 1
                    dq.append([dx, dy, left_horse_move])
    
    return -1

        
print(bfs())
