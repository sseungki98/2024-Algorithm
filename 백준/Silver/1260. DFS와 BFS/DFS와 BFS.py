from collections import defaultdict, deque
N, M, V = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs_visited = []
def dfs(start_node):
    dfs_visited.append(start_node)
    sorted_item = sorted(graph[start_node])
    for item in sorted_item:
        if item not in dfs_visited:
            dfs(item)
            dfs_visited.append(item)
            dfs_visited.pop()

def bfs(start_node):
    bfs_visited = [start_node]
    dq = deque()
    dq.append(start_node)
    while dq:
        node = dq.popleft()
        for item in sorted(graph[node]):
            if item not in bfs_visited:
                dq.append(item)
                bfs_visited.append(item)
    return bfs_visited


dfs(V)
print(*dfs_visited)
print(*bfs(V))

