import sys

input = sys.stdin.readline

n = int(input())

dp = [(0, 0)] * 46
dp[1] = (0, 1)
dp[2] = (1, 1)

for i in range(3, len(dp)):
    a_cnt = dp[i - 1][0]
    b_cnt = dp[i - 1][1]

    dp[i] = (b_cnt, b_cnt + a_cnt)

print(dp[n][0], dp[n][1])