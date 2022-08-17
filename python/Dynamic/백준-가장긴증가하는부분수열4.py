import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * 1001
result = [[] for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                result[i].append(arr[j])
    result[i].append(arr[i])

print(max(dp))

for i in range(0, len(result)):
    if len(result[i]) == max(dp):
        result[i].sort()
        for j in range(0, len(result[i])):
            print(result[i][j], end=' ')
        break