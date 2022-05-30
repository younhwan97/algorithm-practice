def solution(n, lost, reserve):
    answer = 0

    for student in range(1, n + 1):
        if student in lost:
            ## 체육복을 잃어버린 학생
            if student in reserve:
                ## 체육복을 잃어버렸으나 여분을 챙겨왔을 때
                answer += 1            
            else:
                ## 체육복을 잃어버리고 여분도 챙겨오지 않았을 때    
                if student - 1 in reserve and student - 1 not in lost:
                    ## 앞 사람이 체육복을 잃어버리지 않고, 여분을 챙겨왔을 때
                    answer += 1
                elif student + 1 in reserve and student + 1 not in lost:
                    ## 뒷 사람이 체육복을 잃어버리지 않고, 여분을 챙겨왔을 때
                    answer += 1
                    reserve.remove(student + 1)
        else:
            answer += 1

    return answer