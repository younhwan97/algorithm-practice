import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dp = [-1] * 10_001
dp[0] = 0
dp[1] = 1

def fibo(n):
    if dp[n] != -1:
        return dp[n]

    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]

n = int(input())

print(fibo(n))