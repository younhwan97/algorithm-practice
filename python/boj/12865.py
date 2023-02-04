import sys
input = sys.stdin.readline

dp = [[0] * 100_001 for _ in range(101)]

def search(index, w, N, K):
    if dp[index][w] != 0: return dp[index][w]
    if index >= N:
        return 0
    
    n1 = 0 # 
    if (w + arr[index][0] <= K):
        n1 = arr[index][1] + search(index + 1, w + arr[index][0], N, K)
    n2 = search(index + 1, w, N, K)

    dp[index][w] = max(n1, n2)
    return dp[index][w]

N, K = map(int, input().split())
arr = list()
for _ in range(N):
    w, v = map(int, input().split())
    arr.append((w, v))

print(search(0, 0, N, K))