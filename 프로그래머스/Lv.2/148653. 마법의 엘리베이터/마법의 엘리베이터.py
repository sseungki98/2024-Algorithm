import math
def solution(storey):
    answer = 0
    s_storey = list(map(int, str(storey)))
    length = len(s_storey)
    for i in range(length-1, -1, -1): # 3, 2, 1, 0
        s_storey = list(map(int, str(storey)))
        print(s_storey)
        if i == 0:
            if s_storey[i] >= 6:
                answer += (11-s_storey[i])
            else:
                answer += s_storey[i]
            break
        else:
            size = int(math.pow(10, length - 1 - i))
            if s_storey[i] < 5:
                storey -= (s_storey[i] * size)
                answer += s_storey[i]
                
            elif s_storey[i] > 5:
                storey += ((10-s_storey[i]) * size)
                answer += (10 - s_storey[i])
            else:
                if s_storey[i-1] <= 4:
                    storey -= (s_storey[i] * size)
                    answer += s_storey[i]
                else:
                    storey += ((10-s_storey[i]) * size)
                    answer += (10 - s_storey[i])
            
    
    return answer