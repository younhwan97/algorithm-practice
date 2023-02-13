import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(101)]
for i in range(1, 10): dp[1][i] = 1

for i in range(2, 101):
    dp[i][0] = dp[i - 1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j -1] + dp[i - 1][j + 1]
    dp[i][9] = dp[i - 1][8]

print(sum(dp[n]) % 1_000_000_000)