import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1_001
dp[1] = 10

for i in range(2, n + 1):
    dp[i] = () % 10_007
    
print(dp[n])