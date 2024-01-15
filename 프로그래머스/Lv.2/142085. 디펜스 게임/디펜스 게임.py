import heapq
def solution(n, k, enemy):
    answer = 0
    sum = 0
    stack = []
    for item in enemy:
        sum += item
        heapq.heappush(stack, -item)
        if sum > n:
            if k == 0:
                break
            else:
                sum -= (-heapq.heappop(stack))
                k -= 1
                answer += 1
        else:
            answer += 1
        
        
    return answer