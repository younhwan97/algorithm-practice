def func(record):
    if record == 0:
        return 1
    elif record == 1:
        return 2
    return 0

def solution(recordA, recordB):
    cnt = 0
    for i in range(len(recordA)):
        if recordA[i] == recordB[i]: ## 비긴 경우
            continue
        elif recordA[i] == func(recordB[i]): ## 이긴경우
            cnt = cnt + 3
        else:
            if cnt > 0: ## 현재 위치가 제일 아래가 아닐때만
                cnt = cnt - 1 ## 진 경우
    return cnt

#The following is code to output testcase. The code below is correct and you shall correct solution function.
recordA = [2,0,0,0,0,0,1,1,0,0]
recordB = [0,0,0,0,2,2,0,2,2,2]
ret = solution(recordA, recordB)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")