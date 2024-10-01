from collections import defaultdict, deque
import sys

N, M = map(int, sys.stdin.readline().split())  # N: 정점, M: 간선
graph = defaultdict(list)

# 간선 입력 받기
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = set()  # 방문한 정점을 저장하는 집합

# BFS 함수
def bfs(start_node):
    dq = deque([start_node])
    visited.add(start_node)
    while dq:
        node = dq.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dq.append(neighbor)

# 연결 요소 개수 세기
connected_components = 0
for i in range(1, N + 1):  # 1부터 N까지 모든 정점을 확인
    if i not in visited:
        bfs(i)
        connected_components += 1

print(connected_components)
