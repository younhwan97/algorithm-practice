import sys

T = int(sys.stdin.readline())
dp = [0] * (11)

dp[1] = 0
dp[2] = 1
dp[3] = 3



for _ in range(T):
    n = int(sys.stdin.readline())