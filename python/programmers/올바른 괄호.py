def solution(s):
    answer = True
    
    stk = []
    
    for i in s:
        if not stk:
            if i == "(":
                stk.append(i)
            else:
                answer = False
                break
        else:
            if i == "(":
                stk.append(i)
            else:
                top = stk.pop()
                if top != "(":
                    answer = False
                    break
    if stk:
        answer = False
        
    return answer