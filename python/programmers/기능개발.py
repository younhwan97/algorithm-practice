def solution(progresses, speeds):
    answer = []
    
    tmp = 100 - progresses[0]
    if tmp % speeds[0] == 0:
        tmp = tmp // speeds[0]
    else:
        tmp = tmp // speeds[0] + 1
        
    cnt = 1
    for i in range(1, len(speeds)):
        if progresses[i] + speeds[i] * tmp >= 100:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            
            tmp = 100 - progresses[i]
            if tmp % speeds[i] == i:
                tmp = tmp // speeds[i]
            else:
                tmp = tmp // speeds[i] + 1
    
    answer.append(cnt)
    return answer