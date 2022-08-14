import sys

input = sys.stdin.readline

t = int(input())

dp = [(-1, -1)] * 41
dp[0] = (0, 1)
dp[1] = (1, 0)

for i in range(2, 41):
    dp[i] = (dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1])

for _ in range(t):
    n = int(input())
    print(dp[n][1], dp[n][0])