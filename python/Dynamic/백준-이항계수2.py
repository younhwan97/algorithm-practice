import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [0] * 1001
dp[0] = 1
dp[1] = n

for i in range(2, n + 1):
    ## nCk-1
    #  n!
    #  (n - k + 1)! * (k - 1)!

    ## nCk
    #  n!
    #  (n - k)! * (k)!

    dp[i] = (dp[i - 1] * (n - i + 1)) // i

print(dp[k] % 10007)