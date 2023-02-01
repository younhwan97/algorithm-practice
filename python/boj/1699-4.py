import sys, math
input = sys.stdin.readline

N = int(input())
dp = [-1] * (100_001)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 1

for i in range(5, 100_001):
    if math.sqrt(i) == int(math.sqrt(i)):
        dp[i] = 1
    else:
        dp[i] = dp[i - 1] + 1

        value = 1
        while value * value <= i:
            dp[i] = min(dp[i - value * value] + 1, dp[i])
            value += 1

print(dp[N])