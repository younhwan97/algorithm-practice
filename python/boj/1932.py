import sys
input = sys.stdin.readline

dp = [[0] * 501 for _ in range(501)]

def search(height, index, cost, arr, N):
    if height + 1 >= N:
        return cost

    if dp[height][index] != 0:
        return dp[height][index]
    
    left = cost + search(height + 1, index, arr[height + 1][index], arr, N)
    right = cost + search(height + 1, index + 1, arr[height + 1][index + 1], arr, N)

    dp[height][index] = max(left, right)
    return dp[height][index]


N = int(input())
arr = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

print(search(0, 0, arr[0][0], arr, N))