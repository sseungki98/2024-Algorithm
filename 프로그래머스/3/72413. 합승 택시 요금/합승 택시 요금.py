from collections import defaultdict
import heapq
def solution(n, s, a, b, fares):
    route = defaultdict(list)

    for item in fares:
        start, end, price = item
        route[start].append([end, price])
        route[end].append([start, price])

    INF = float('inf')

    def dijkstra(start_node):
        distance = [INF] * (n+1)
        distance[start_node] = 0
        hq = []
        heapq.heappush(hq, [start_node, 0])
        while hq:
            node, dist = heapq.heappop(hq)
            if distance[node] < dist:
                continue
            for next in route[node]:
                new_dist = distance[node] + next[1]
                if distance[next[0]] > new_dist:
                    distance[next[0]] = new_dist
                    heapq.heappush(hq, [next[0], new_dist])

        return distance

    dijkstra_list = [[]]
    for i in range(1, n+1):
        dijkstra_list.append(dijkstra(i))

    answer = float('inf')

    for i in range(1, n+1):
        temp_ans = 0
        temp_ans += dijkstra_list[s][i]
        temp_ans += dijkstra_list[i][a]
        temp_ans += dijkstra_list[i][b]

        answer = min(answer, temp_ans)

    return answer