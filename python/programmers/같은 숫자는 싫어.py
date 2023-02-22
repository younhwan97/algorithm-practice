def solution(arr):
    answer = []

    for value in arr:
        if not answer:
            answer.append(value)
        else:
            tmp = answer.pop()
            if tmp != value:
                answer.append(tmp)
                answer.append(value)
            else:
                answer.append(tmp)
            
    return answer