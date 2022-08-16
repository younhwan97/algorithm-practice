import sys

input = sys.stdin.readline

dp = [""] * 10001

dp[1] = "CY"
dp[2] = "SK"
dp[3] = "CY"
dp[4] = "SK"
dp[5] = "CY"

for i in range(6, 1001):
    if dp[i - 1] == "CY" or dp[i - 3] == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"
     
n = int(input())
print(dp[n])