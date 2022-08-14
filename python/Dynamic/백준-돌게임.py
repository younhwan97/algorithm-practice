import sys

input = sys.stdin.readline

n = int(input())

dp = [""] * 10001

dp[1] = "SK"
dp[2] = "CY"
dp[3] = "SK"
dp[4] = "CY"
dp[5] = "SK"

for i in range(6, len(dp)):
    dp[i] = "SK" if dp[i - 1] == "CY" else "CY"

print(dp[n])