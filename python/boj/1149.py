import sys
input = sys.stdin.readline

N = int(input())
prices = list()
for _ in range(N):
    p1, p2, p3 = map(int, input().split())
    prices.append((p1, p2, p3))
    
dp = [[0] * 3 for _ in range(N)]
dp[0][0] = prices[0][0] # 0번 인덱스 -> 빨간 색으로 집을 칠한 경우
dp[0][1] = prices[0][1] # 1번 인덱스 -> 초록 색으로 집을 칠한 경우
dp[0][2] = prices[0][2] # 2번 인덱스 -> 파란 색으로 집을 칠한 경우

for i in range(1, N):
    dp[i][0] = prices[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = prices[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = prices[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N - 1]))