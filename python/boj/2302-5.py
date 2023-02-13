import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
vip = set()

for _ in range(K):
    value = int(input())
    vip.add(value)

dp = [[0] * 3 for _ in range(N + 1)]

if 1 not in vip:
    dp[1][0] = 1 # 자기 자리에 앉는 경우
    dp[1][1] = 0 # 자기보다 앞자리에 앉는 경우
    dp[1][2] = 1 # 자기보다 뒷자리에 앉는 경우
else:
    dp[1][0] = 1

for i in range(2, N + 1):
    if i in vip:
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
    else:
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][2]
        
        if i + 1 not in vip:
            dp[i][2] = dp[i][0]

dp[-1][2] = 0

print(sum(dp[N]))