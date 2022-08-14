import sys

input = sys.stdin.readline

dp = [-1] * 81
dp[1] = 1
dp[2] = 1

def fibo(n):
    if dp[n] != -1:
        return dp[n]

    dp[n] = fibo(n - 1) + fibo(n - 2)
    return dp[n]

fibo(80)

dp2 = [-1] * 81
dp2[1] = 4
dp2[2] = 6
dp2[3] = 10
dp2[4] = 16
dp2[5] = 26

for i in range(6, len(dp2)):
    dp2[i] = dp2[i - 1] + 2 * dp[i]

n = int(input())

print(dp2[n])