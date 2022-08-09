import sys
sys.setrecursionlimit(10 ** 6)

## 입력
input = sys.stdin.readline

n = int(input())

## 메모이제이션을 이용해 dp 초기화
dp = [0] * 48
def fibo(n):
    if dp[n] != 0:
        return dp[n]

    if n == 0:
        dp[0] = 0
        return dp[0]
    elif n == 1:
        dp[1] = 1
        return dp[1]
    else:
        dp[n] = fibo(n - 1) + fibo(n - 2)
        return dp[n]

fibo(47)

## 테스트 케이스에 따른 답 출력
for t in range(n):
    num = int(input())

    index = -1
    for i in range(100):
        if dp[47 - i - 1] <= num:
            index = 47 - i - 1
            break

    result = list()
  
    for i in range(index):
        if sum(result) + dp[index - i] <= num:
            result.append(dp[index - i])
            if sum(result) == num:
                break
    
    result.reverse()

    for i in range(len(result)):
        print(result[i], end=' ')