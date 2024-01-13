
def solution(sequence, k):
    answer = []
    l = 0
    r = -1
    sum = 0
    
    while True:
        if sum < k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
            
        else:
            if r >= len(sequence):
                break
            sum -= sequence[l]
            l += 1
            
        if sum == k:
            answer.append([l, r])
    
    new_list = sorted(answer, key=lambda x:((x[1] - x[0]),x[0]))
    
    return new_list[0]