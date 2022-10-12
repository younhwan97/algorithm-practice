import math

def get_primes(n):
    a = [0] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if a[i] == 0:
            for x in range(i + i, n + 1, i):
                a[x] = 1
    
    primes = []
    for i in range(2, n + 1):
        if a[i] == 0:
            primes.append(i)
    return primes

def solution(n):
    primes = get_primes(1000)

    cnt = [[0] * 3000 for _ in range(4)]

    for i in range(len(primes)):
        cnt[1][primes[i]] = 1

        for j in range(2, 0, -1):
            for k in range(3000):
                if j == 1 and primes[i] == k:
                    continue
                    
                if cnt[j][k] > 0:
                    cnt[j + 1][k + primes[i]] += cnt[j][k]

    return cnt[3][n]
    
#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 33
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")