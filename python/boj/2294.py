import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = set()
for _ in range(N):
    arr.add(int(input()))

dp = [-1] * (K + 1)
dp[0] = 0

sorted_arr = []
for i in arr: sorted_arr.append(i)
sorted_arr.sort()

for i in sorted_arr:
    for j in range(i, K + 1):
        if j - i >= 0 and dp[j - i] != -1:
            if dp[j] == -1:
                dp[j] = dp[j - i] + 1
            else:
                dp[j] = min(dp[j - i] + 1, dp[j])

print(dp[K])