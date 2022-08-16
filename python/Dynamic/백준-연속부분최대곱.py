import sys

input = sys.stdin.readline

n = int(input())

arr = list()

for i in range(n):
    arr.append(float(input()))

dp = [1] * n
dp[0] = arr[0]

for i in range(1, len(dp)):
    dp[i] = max(dp[i - 1] * arr[i], arr[i])

print("{:.3f}".format(max(dp)))