import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp1 = [0] * len(arr)
dp2 = [0] * len(arr)

dp1[0] = 1
dp2[0] = 1

for i in range(1, len(arr)):
    if arr[i] >= arr[i - 1]:
        dp1[i] = dp1[i - 1] + 1
    else:
        dp1[i] = 1

    if arr[i] <= arr[i - 1]:
        dp2[i] = dp2[i - 1] + 1
    else:
        dp2[i] = 1

print(max(max(dp1), max(dp2)))