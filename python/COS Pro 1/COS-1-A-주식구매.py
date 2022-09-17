def solution(prices):
    INF = 1_000_000_001
    tmp = INF # 큰 수를 초기 값으로 -> 작은 수를 찾을 때
    answer = -INF # 작은 수를 초기 값으로 -> 큰 수를 찾을 때
    for price in prices:
        if tmp != INF:
            answer = max(answer, price - tmp)
        tmp = min(tmp, price)
    return answer

#The following is code to output testcase. The code below is correct and you shall correct solution function.
prices1 = [1, 2, 3]
ret1 = solution(prices1)

#Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")
    
prices2 = [3, 1]
ret2 = solution(prices2)

#Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")