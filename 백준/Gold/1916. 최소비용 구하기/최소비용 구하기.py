from collections import deque, defaultdict
import heapq

N = int(input())
M = int(input())
INF = float('inf')
route = defaultdict(list)
distance = [INF] * (N+1)

for _ in range(M):
    temp = list(map(int, input().split()))
    u, v, _dist = temp[0], temp[1], temp[2]
    route[u].append([_dist, v])
    # route[v].append([_dist, u])

target = list(map(int, input().split()))
start, end = target[0], target[1]
def dijkstra(start_node):
    distance[start_node] = 0
    hq = []
    heapq.heappush(hq, [0, start_node])
    while hq:
        dist, node = heapq.heappop(hq)
        if distance[node] < dist:
            continue
        for next in route[node]:
            cost = distance[node] + next[0]
            if distance[next[1]] > cost:
                distance[next[1]] = cost
                heapq.heappush(hq, [cost, next[1]])

dijkstra(start)
print(distance[end])
