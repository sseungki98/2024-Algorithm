import math
def solution(number, limit, power):
    answer = 0
    for j in range(1, number+1):
        answer_list = set()
        pivot = math.floor(math.sqrt(number))
        for i in range(1, pivot+1):
            if j % i == 0:
                answer_list.add(i)
                answer_list.add(j // i)
        
        if len(answer_list) <= limit:
            answer += len(answer_list)
        else:
            answer += power
        
    return answer