import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * 1001
dp[1] = arr[0]
dp[2] = arr[1] if arr[1] > arr[0] * 2 else arr[0] * 2

for i in range(3, n + 1):
    dp[i] = arr[i - 1]

    for j in range(1, i):
        dp[i] = max(dp[i], dp[i - j] + dp[j])

print(dp[n])