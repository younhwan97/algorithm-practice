import math

def solution(brown, yellow):
    answer = []
    
    size = brown + yellow
    tmp = int(math.sqrt(size))
    
    while True:
        if (size // tmp) * 2 + (tmp - 2) * 2 == brown:
            break
        else:
            tmp += 1
    
    answer.append(tmp)
    answer.append(size // tmp)
    answer.sort(reverse = True)
    
    return answer