import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list()
dp = [-1] * 10_001

for _ in range(n):
    value = int(input())
    arr.append(value)
    dp[value] = 1

def go(value):
    global arr

    if dp[value] != -1:
        return dp[value]

    if value <= 0:
        return 0

    cnt = 0
    for i in range(len(arr)):
        cnt += go(value - arr[i])

    dp[value] = cnt
    return cnt

go(k)
print(dp[:20])
