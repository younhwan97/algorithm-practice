#You may use import as below.
#import math

def solution(num):
    # Write code here.
    answer = num

    answer += 1
    answer = str(answer)
    ## replace(old, new, count)
    ### count의 기본값은 -1로 전체를 의미한다.
    answer = answer.replace('0', '1')
    
    return answer

#The following is code to output testcase.
num = 999
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")