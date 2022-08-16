import sys

input = sys.stdin.readline

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7
dp[10] = 9
dp[11] = 12

for i in range(12, len(dp)):
    dp[i] = dp[i - 1] + dp[i - 5]

t = int(input())

for i in range(t):
    n = int(input())
    print(dp[n])