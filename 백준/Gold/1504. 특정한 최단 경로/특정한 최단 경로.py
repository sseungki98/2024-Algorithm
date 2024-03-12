from collections import defaultdict
import sys
import heapq
N, E = map(int, input().split())
route = defaultdict(list)

for _ in range(E):
    start, end, cost = map(int, sys.stdin.readline().split())
    route[start].append([end, cost])
    route[end].append([start, cost])

travel_node = list(map(int, input().split()))

def dijkstra(start_node):
    dist = [float('inf')] * (N+1)
    dist[start_node] = 0
    hq = []
    heapq.heappush(hq, (start_node, 0))
    while hq:
        node, dist_cost = heapq.heappop(hq)
        if dist[node] < dist_cost:
            continue
        for next in route[node]:
            cost = dist_cost + next[1]
            if dist[next[0]] > cost:
                dist[next[0]] = cost
                heapq.heappush(hq, [next[0], cost])

    return dist


zero_dists = dijkstra(1)
first_dists = (dijkstra(travel_node[0]))
second_dists = (dijkstra(N))

first_route = zero_dists[travel_node[0]] + first_dists[travel_node[1]] + second_dists[travel_node[1]]
second_route = zero_dists[travel_node[1]] + first_dists[travel_node[1]] + second_dists[travel_node[0]]
answer = min(first_route, second_route)
if answer != float('inf'):
    print(answer)
else:
    print(-1)


