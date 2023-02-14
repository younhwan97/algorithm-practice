import sys, math
input = sys.stdin.readline

N = int(input())
dp = [5] * 50_001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 1
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 2

for i in range(9, 50_001):
    if math.sqrt(i) == int(math.sqrt(i)):
        dp[i] = 1
        continue
    
    for j in range(1, 224):
        if dp[i - j * j] + 1 <= 4:
            dp[i] = min(dp[i], dp[i - j * j] + 1)

        if dp[i] == 2:
            break
    
print(dp[N])