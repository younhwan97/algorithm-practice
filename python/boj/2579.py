import sys
input = sys.stdin.readline

N = int(input())
arr = list()
for _ in range(N): arr.append(int(input()))

dp = [0] * (301)
dp[0] = arr[0]

if N > 1:
    dp[1] = arr[0] + arr[1]

if N > 2:
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, N):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

print(dp[N - 1])