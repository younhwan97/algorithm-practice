import math

def get_primes(n):

    a = [0] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if a[i] == 0:
            for x in range(i + i, n + 1, i):
                a[x] = 1 ## 값이 1이면 소수가 될 수 없는 수
    
    primes = []

    for i in range(2, n + 1):
        if a[i] == 0:
            primes.append(i)

    return primes

def solution(n):
    answer = 0
    primes = get_primes(n)

    prime_len = len(primes)
    for i in range(0, prime_len - 2) :
        for j in range(i + 1, prime_len - 1) :
            for k in range(j + 1, prime_len) :
                if primes[i] + primes[j] + primes[k] == n:
                    answer += 1
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 33
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 9
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")