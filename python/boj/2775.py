import sys
input = sys.stdin.readline

dp = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    dp[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

# 0 1 3 6 
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14

T = int(input())
for _ in range(T):
    n = int(input())
    k = int(input())

    print(dp[n][k])