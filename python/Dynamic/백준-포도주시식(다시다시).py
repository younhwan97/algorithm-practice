import sys
input = sys.stdin.readline

n = int(input())

arr = list()
for _ in range(n): arr.append(int(input()))

dp = [0] * 10_001
dp[1] = arr[0]

if n > 1:
    dp[2] = dp[1] + arr[1]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + arr[i - 2]) + arr[i - 1]
        dp[i] = max(dp[i], dp[i - 1])

print(max(dp))