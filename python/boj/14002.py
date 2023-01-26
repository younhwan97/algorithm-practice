import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[] for _ in range(n)]
dp[0].append(arr[0])

for i in range(1, n):
    for j in range(i):
        if dp[j] and dp[j][-1] < arr[i]:
            tmp = dp[j].copy()
            tmp.append(arr[i])
    
            if len(dp[i]) < len(tmp):
                dp[i] = tmp
    
    if not dp[i]:
        dp[i].append(arr[i])

ans = len(dp[0])
result = dp[0].copy()
for i in range(1, n):
    if len(dp[i]) > ans:
        ans = len(dp[i])
        result = dp[i].copy()

print(ans)
for i in range(ans):
    print(result[i], end=" ")