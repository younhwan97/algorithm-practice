import sys
input = sys.stdin.readline

N, S, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0] * (M+ 1) for _ in range(N + 1)]

def go(index, now):
    global M, N

    if dp[index][now] != 0:
        return dp[index][now]

    if index == N:
        return now

    # 볼륨을 올릴 때
    n1 = -1
    if now + arr[index] <= M:
        n1 = go(index + 1, now + arr[index])

    # 볼륨을 내릴 때
    n2 = -1
    if now - arr[index] >= 0:
        n2 = go(index + 1, now - arr[index])

    dp[index][now] = max(n1, n2)
    return dp[index][now]

ans = go(0, S)

print(ans)

# dp = [[0] * (M + 1) for _ in range(N + 1)]

# def go(index, value):
#     global arr, M, N

#     if dp[index][value] != 0:
#         return dp[index][value]

#     if index == N:
#         return value

#     if dp[index][value] == -1:
#         return -1

#     n1 = -1
#     if (value + arr[index] <= M):
#         n1 = go(index + 1, value + arr[index])
    
#     n2 = -1
#     if (value - arr[index] >= 0):
#         n2 = go(index + 1, value - arr[index])

#     dp[index][value] = max(n1, n2)
#     return dp[index][value]

# print(go(0, S))