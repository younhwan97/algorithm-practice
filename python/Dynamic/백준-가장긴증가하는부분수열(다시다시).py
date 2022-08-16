import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [1] * 1001

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))