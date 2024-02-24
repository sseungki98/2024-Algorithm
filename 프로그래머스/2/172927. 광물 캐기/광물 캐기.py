from collections import deque
def solution(picks, minerals):
    def calcPiro(mine, pick):
        piro = 0
        for item in mine:
            if pick == 'diamond':
                piro += 1
            if pick == 'iron':
                if item == 'diamond':
                    piro += 5
                else:
                    piro += 1
            if pick == 'stone':
                if item == 'diamond':
                    piro += 25
                elif item == 'iron':
                    piro += 5
                else:
                    piro += 1
        return piro
    answer = 0
    minerals_len = len(minerals)
    mok = minerals_len // 5
    na = minerals_len % 5
    mineral_array = []
    for i in range(mok):
        mineral_array.append(minerals[i*5:(i+1)*5])
    mineral_array.append(minerals[mok*5:mok*5+na])
    pick_sum = sum(picks)
    mineral_array = mineral_array[0:pick_sum]
    def count_elements(subarray):
        counts = {'diamond': 0, 'iron': 0, 'stone': 0}
        for item in subarray:
            counts[item] += 1
        return counts

# 각 하위 배열의 원소를 정렬하는 함수
    def custom_sort(subarray):
        counts = count_elements(subarray)
        return (-counts['diamond'], -counts['iron'], -counts['stone'])

    sorted_array = sorted(mineral_array, key=custom_sort)

    for item in sorted_array:
        if picks[0] != 0:
            answer += calcPiro(item, 'diamond')
            picks[0] -= 1
            continue
        if picks[1] != 0:
            answer += calcPiro(item, 'iron')
            picks[1] -= 1
            continue
        if picks[2] != 0:
            answer += calcPiro(item, 'stone')
            picks[2] -= 1
            continue

    return answer