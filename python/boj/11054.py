import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp1 = [1] * N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

dp2 = [1] * N
arr = arr[::-1]
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2 = dp2[::-1]
ans = [0] * N
for i in range(N):
    ans[i] = dp1[i] + dp2[i] - 1

print(max(ans))