import sys
input = sys.stdin.readline

dp = [[0] * 10 for _ in range(1001)]

dp[1][0] = 10

for i in range(0, 10):
    dp[2][i] = 10 - i

n = int(input())

for i in range(3, n + 1):
    for j in range(0, 10):
        for k in range(j, 10):
            dp[i][j] += dp[i - 1][k]

print(sum(dp[n]) % 10007)

# 단순 재귀로 풀이하면 왜 안될까?
## 시간복잡도 10 ^ N .... 