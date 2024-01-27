from itertools import permutations
def solution(k, dungeons):
    answer = -1
    cb = list(permutations(dungeons, len(dungeons)))
    for item in cb:
        temp_k = k
        temp_count = 0
        for dg in item:
            if temp_k >= dg[0]:
                temp_count += 1
                temp_k -= dg[1]
            else:
                break
        answer = max(answer, temp_count)
    return answer