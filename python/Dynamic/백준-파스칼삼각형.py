import sys

input = sys.stdin.readline

dp = []

dp.append([])
dp.append([1])
dp.append([1, 1])

for i in range(3, 31):
    temp = [0] * i

    temp[0] = 1
    temp[len(temp) - 1] = 1

    for j in range(1, i - 1):
        temp[j] = dp[len(dp) - 1][j - 1] + dp[len(dp) - 1][j]
    
    dp.append(temp)

n, k = map(int, input().split())
print(dp[n][k - 1])