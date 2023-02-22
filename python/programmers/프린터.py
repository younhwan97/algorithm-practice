from collections import deque

def solution(priorities, location):
    answer = 0
    
    que = deque()
    for i in range(len(priorities)):
        que.append((priorities[i], i))

    cnt = 1
    while que:
        value, index = que.popleft()
        
        flag = True
        for i in range(len(que)):
            if que[i][0] > value:
                flag = False
                break
        
        if not flag:
            que.append((value, index))
        else:
            if location == index:
                answer = cnt
                break
            cnt += 1
        
    return answer