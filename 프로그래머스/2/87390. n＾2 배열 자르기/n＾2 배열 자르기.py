def solution(n, left, right):
    answer = []
    start_row = left // n
    end_row = right // n
    start_col = left % n
    end_col = right % n
    print(start_row,end_row,start_col,end_col)
    for i in range(start_row+1, end_row+2):
        f_list = [i for i in range(1, n+1)]
        temp_list = [i] * i + f_list[i:]
        answer += temp_list

    return answer[start_col:(end_row - start_row) * n +end_col+1]
