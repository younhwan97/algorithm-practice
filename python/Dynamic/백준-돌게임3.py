import sys

input = sys.stdin.readline

dp = [""] * 10001

dp[1] = "SK"
dp[2] = "CY"
dp[3] = "SK"
dp[4] = "SK"
dp[5] = "SK"

for i in range(6, 1001):
    if dp[i - 4] == "CY" or dp[i - 3] == "CY" or dp[i - 1] == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"
     
n = int(input())
print(dp[n])