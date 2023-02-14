import sys
input = sys.stdin.readline

N = int(input())
arr = list()
for _ in range(N):
    need, price = map(int, input().split())
    arr.append((need, price))

dp = [0] * (N + 1)

for i in range(0, N):
    if i + arr[i][0] <= N:
        dp[i + arr[i][0]] = max(dp[i + arr[i][0]], dp[i] + arr[i][1])
    
    if i + 1 <= N:
        dp[i + 1] = max(dp[i + 1], dp[i])
    
print(dp[N])