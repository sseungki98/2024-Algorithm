from collections import deque
N = int(input())
stone = list(map(int, input().split()))
a, b = map(int, input().split())


def bfs():
    dq = deque([a-1])
    visited = [-1] * 10000
    visited[a-1] = 0
    while dq:
        target = dq.popleft()
        for i in range(target, N, stone[target]):
            if visited[i] == -1:
                dq.append(i)
                visited[i] = visited[target] + 1

                if i == b-1:
                    return visited[i]

        for i in range(target, -1, -stone[target]):
            if visited[i] == -1:
                dq.append(i)
                visited[i] = visited[target] + 1

                if i == b-1:
                    return visited[i]

    return -1


print(bfs())


