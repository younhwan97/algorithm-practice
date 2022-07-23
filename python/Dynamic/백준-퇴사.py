import sys, heapq

N = int(input())
dp = [0] * 16

for i in range(1, N + 1):
    d, p = map(int, sys.stdin.readline().split())

    if i + d <= N:
        dp[i] = 

