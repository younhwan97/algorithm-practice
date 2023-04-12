import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 입력
N, K = map(int, input().split())

# DP 구하기
dp = [-1] * (100_001)
dp[N] = 0

for i in range(N - 1, -1, -1):
    dp[i] = dp[i + 1] + 1

for i in range(N + 1, 100_001):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i // 2] != -1:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if (i + 1) % 2 == 0 and dp[(i + 1) // 2] != -1:
        dp[i] = min(dp[i], dp[(i + 1) // 2] + 2)

# DP 리스트를 DFS 탐색
result = []
def dfs(current, path):
    global result

    if result: return

    if current == N:
        result = copy.deepcopy(path)
        return
    
    # -1
    if current + 1 < len(dp) and dp[current] - 1 == dp[current + 1]:
        path.append(current + 1)
        dfs(current + 1, path)
        path.pop()

    # +1
    if current - 1 < len(dp) and dp[current] - 1 == dp[current - 1]:
        path.append(current - 1)
        dfs(current - 1, path)
        path.pop()

    # x2
    if current % 2 == 0 and dp[current] - 1 == dp[current // 2]:
        path.append(current // 2)
        dfs(current // 2, path)
        path.pop()

dfs(K, [K])

# 결과
print(dp[K])
print(' '.join(map(str, result[::-1])))