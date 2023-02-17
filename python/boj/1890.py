import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

dp = [[0] * n for _ in range(n)]

def go(x, y):
    global n, arr

    if dp[x][y] != 0:
        return dp[x][y]

    if x == n - 1 and y == n - 1:
        return 1

    # right
    right = 0
    if arr[x][y] != 0 and y + arr[x][y] < n:
        right = go(x, y + arr[x][y])

    # bottom
    bottom = 0
    if arr[x][y] != 0 and x + arr[x][y] < n:
        bottom = go(x + arr[x][y], y)

    dp[x][y] = right + bottom
    return dp[x][y]

print(go(0,0))

# def go(x, y):
#     global arr, n

#     if dp[x][y] != 0:
#         return dp[x][y]
    
#     if x == n - 1 and y == n - 1:
#         return 1
    
#     # 오른쪽
#     n1 = 0
#     if arr[x][y] != 0 and y + arr[x][y] < n:
#         n1 = go(x, y + arr[x][y])
    
#     # 아래쪽
#     n2 = 0
#     if arr[x][y] != 0 and x + arr[x][y] < n:
#         n2 = go(x + arr[x][y], y)

#     dp[x][y] = n1 + n2
#     return dp[x][y]

# print(go(0, 0))