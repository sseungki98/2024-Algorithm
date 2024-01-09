from collections import deque
def solution(maps):
    MAX = 1000000
    answer = 0
    l_map = []
    len_x = len(maps)
    len_y = len(maps[0])
    for item in maps:
        l_map.append(list(item))
    step = [[MAX for _ in range(len_y)] for _ in range(len_x)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    exit_x = ''
    exit_y = ''
    laver_x = ''
    laver_y = ''
    for i in range(len_x):
        for j in range(len_y):
            if l_map[i][j] == 'E':
                exit_x = i
                exit_y = j
            elif l_map[i][j] == 'L':
                laver_x = i
                laver_y = j
    
    
    def bfs(i, j):
        dq = deque()
        dq.append((i, j))
        step[i][j] = 0
        while dq:
            x, y = dq.popleft()
            for i in range(4):
                ddx = x + dx[i]
                ddy = y + dy[i]
                if 0<=ddx<len_x and 0<=ddy<len_y:
                    if l_map[ddx][ddy] != 'X':
                        dq.append((ddx, ddy))
                        step[ddx][ddy] = min(step[ddx][ddy], step[x][y] + 1)
                        l_map[ddx][ddy] = 'X'
                        
    for item in maps:
        l_map.append(list(item))
    
    for i in range(len_x):
        for j in range(len_y):
            if l_map[i][j] == 'S':
                bfs(i, j)
    
    temp_to_laver = 0

    if step[laver_x][laver_y] == MAX:
        return -1
    else:
        temp_to_laver = step[laver_x][laver_y]
        step = [[MAX for _ in range(len_y)] for _ in range(len_x)]
        l_map = []
        for item in maps:
            l_map.append(list(item))
        bfs(laver_x, laver_y)

        if step[exit_x][exit_y] == MAX:
            return -1
        else:
            return step[exit_x][exit_y] + temp_to_laver


    
