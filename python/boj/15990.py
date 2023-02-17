import sys
input = sys.stdin.readline

dp = [[0] * 4 for _ in range(100_001)] 
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1 

for i in range(4, 100_001):
    # +3
    dp[i][3] = dp[i - 3][1] % 1_000_000_009 + dp[i - 3][2] % 1_000_000_009

    # +2
    dp[i][2] = dp[i - 2][1] % 1_000_000_009 + dp[i - 2][3] % 1_000_000_009

    # +1
    dp[i][1] = dp[i - 1][2] % 1_000_000_009 + dp[i - 1][3] % 1_000_000_009
    

t = int(input())
for _ in range(t):
    n = int(input())

    

    print((dp[n][1] + dp[n][2] + dp[n][3]) % 1_000_000_009)