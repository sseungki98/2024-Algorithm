import math
def solution(k, d):
    answer = 0
    stack = []
    t = d // k
    stack.append(t+1)
    for i in range(1, t+1):
        x_idx = int(math.sqrt(math.pow(d,2) - math.pow(i*k,2)))
        stack.append(x_idx // k + 1)

    return sum(stack)