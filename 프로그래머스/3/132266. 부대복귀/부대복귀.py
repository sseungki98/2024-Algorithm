from collections import deque, defaultdict
def solution(n, roads, sources, destination):
    answer = []
    route = defaultdict(list)
    for road in roads:
        route[road[0]].append(road[1])
        route[road[1]].append(road[0])
    
    visited = [[False, 0] for _ in range(n+1)]
    def bfs(s_node):
        dq = deque()
        dq.append(s_node)
        visited[s_node][0] = True
        
        while dq:
            node = dq.popleft()
            for way in route[node]:
                if visited[way][0] == False:
                    visited[way][0] = True
                    visited[way][1] = visited[node][1] + 1
                    dq.append(way)

    bfs(destination)
    for src in sources:
        if src == destination:
            answer.append(0)
            continue
        if visited[src][1] == 0:
            answer.append(-1)
        else:
            answer.append(visited[src][1])
        
        
    return answer