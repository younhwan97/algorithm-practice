#다음과 같이 import를 사용할 수 있습니다.
import math
from re import L

def solution(a, b):
    # 여기에 코드를 작성해주세요.
    e = int(math.sqrt(b))
    primes = [1] * (e + 1)
    prime_list = []
    for i in range(2, e + 1):
        if primes[i] == 1:
            prime_list.append(i)

            for j in range(i + i, e + 1, i):
                primes[j] = 0
    
    answer = 0
    for i in range(len(prime_list)):
        if a <= prime_list[i] ** 2 <= b:
            answer += 1
        
        if a <= prime_list[i] ** 3 <= b:
            answer += 1

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  30
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")