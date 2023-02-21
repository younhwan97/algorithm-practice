result = set()

def search(now, numbers, cnt, used):
    global result
    
    if cnt == len(numbers):
        result.add(int(now)) 
        return
    
    for i in range(len(numbers)):
        if i not in used:
            used.add(i)
            search(now + numbers[i], numbers, cnt + 1, used)
            used.remove(i)
        else:
            search("0" + now, numbers, cnt + 1, used)

def solution(numbers):
    global result
    
    search("", numbers, 0, set())
    answer = 0
    
    for i in result:
        if i >= 2:
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break

            if flag:
                answer += 1
  
    return answer