import sys
input = sys.stdin.readline

n = int(input())

dp = list()

for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, len(dp)):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][0] += dp[i - 1][0]
        elif j + 1 == len(dp[i]):
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1]) 

print(max(dp[n-1]))