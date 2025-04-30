def solution(schedules, timelogs, startday):
    answer = 0
    m_schedule = []
    for schedule in schedules:
        if (schedule % 100) + 10 >= 60:
            n_schedule = (schedule // 100 + 1) * 100 + ((schedule % 100 + 10) - 60)
            m_schedule.append(n_schedule)
        else:
            m_schedule.append(schedule+10)
    
    for i in range(len(timelogs)):
        day_count = 0
        day = startday
        flag = True

        for tl in timelogs[i]:
            if day == 6 or day == 7:
                day += 1
                if day == 8:
                    day = 1
                day_count += 1
                continue
            else:
                if tl > m_schedule[i]:
                    flag = False
                    break
                else:
                    day += 1
                    day_count += 1
        
        if flag == True:
            answer += 1
    return answer