def solution(data, col, row_begin, row_end):
    answer = []
    data.sort(key = lambda x:(x[col-1], -x[0]))

    for i in range(row_begin-1, row_end): #1, 2
        mod_sum = 0
        for item in data[i]:
            mod_sum += item % (i+1)
        answer.append(mod_sum)
    
    temp = answer[0]
    if len(answer) == 1:
        return temp
    else:
        for i in range(1, len(answer)):
            temp = temp^answer[i]
    

        return temp