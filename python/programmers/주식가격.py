def solution(prices):
    answer = []
    stk = []
    result = [0] * len(prices)
    
    for i in range(len(prices)):
        while 1:
            if stk:
                idx, top = stk.pop()
            
                if top <= prices[i]:
                    stk.append((idx, top))
                    stk.append((i, prices[i]))
                    break
                else:
                    if i - idx == 1:
                        result[idx] = 1
                    else:
                        result[idx] = i - idx
            else:
                stk.append((i, prices[i]))
                break

    while stk:
        idx, value = stk.pop()
        result[idx] = len(prices) - idx - 1
        
    answer = result
    return answer