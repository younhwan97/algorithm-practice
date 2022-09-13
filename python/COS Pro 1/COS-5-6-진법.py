#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(s1, s2, p, q):
    #여기에 코드를 작성해주세요.

    ## p -> 10 진법 변환
    s1_temp = 0

    for i in range(len(s1)):
        s1_temp += (p ** i * int(s1[len(s1) - 1 - i]))

    s2_temp = 0    
    for i in range(len(s2)):
        s2_temp += (p ** i * int(s2[len(s2) - 1 - i]))

    s = s1_temp + s2_temp

    ## 10 -> q 진법 변환
    answer = ''

    while s != 0:
        answer = str((s % q)) + answer
        s //= q

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")