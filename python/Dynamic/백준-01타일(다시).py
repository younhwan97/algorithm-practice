import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1_000_001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5

for i in range(5, len(dp)):
    ## dp[1] = 1
    ## dp[2] = 00, 11
    ## dp[3] = 100, 001, 111
    ## dp[4] = 0011, 1100, 0000, 1001, 1111
    ## dp[5] = 10000, 00001 10011, 11001, 11100, 11111,00100 

    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

print(dp[n])