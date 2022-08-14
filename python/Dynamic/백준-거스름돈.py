import sys

input = sys.stdin.readline

n = int(input())

dp = [-1] * 100_001
dp[2] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, len(dp)):
    if dp[i - 2] != -1:
        dp[i] = dp[i - 2] + 1

    if dp[i - 5] != -1 and dp[i - 5] + 1 < dp[i]:
        dp[i] = dp[i - 5] + 1 

print(dp[n])