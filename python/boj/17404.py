import sys
input = sys.stdin.readline

N = int(input())
prices = []
for _ in range(N):
    p1, p2, p3 = map(int, input().split())
    prices.append((p1, p2, p3))

ans = 1000 * 1000 + 1
for i in range(3): # 빨 -> 초 -> 파
    dp = [[0] * 3 for _ in range(N)]

    dp[0][0], dp[0][1], dp[0][2] = prices[0][0], prices[0][1], prices[0][2]

    dp[1][0] = prices[1][0] + dp[0][i]
    dp[1][1] = prices[1][1] + dp[0][i]
    dp[1][2] = prices[1][2] + dp[0][i]

    dp[1][i] = 1000 * 1000 + 1
    
    for j in range(2, N):
        dp[j][0] = prices[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = prices[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = prices[j][2] + min(dp[j - 1][0], dp[j - 1][1])

    dp[N - 1][i] = 1000 * 1000 + 1
    ans = min(ans, min(dp[N - 1]))

print(ans)