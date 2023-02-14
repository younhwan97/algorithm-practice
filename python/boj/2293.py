import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list()

dp = [0] * 10_001
dp[0] = 1

for _ in range(n): arr.append(int(input()))

for i in arr:
    for j in range(1, 10_001):
        if j >= i:
            dp[j] += dp[j - i]

print(dp[k])