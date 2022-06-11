import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    ## 상, 하, 좌, 우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if s[nx][ny] == 1:
                s[nx][ny] = -1
                dfs(nx, ny)
        
T = int(input())
answer = list()

for _ in range(T):
    M, N, K = map(int, input().split())
    s = [[0] * M for _ in range(N)]
    cnt = 0

    for _ in range(K):
        i, j = map(int, input().split())
        s[j][i] = 1

    for i in range(N):
        for j in range(M):
            if s[i][j] > 0:
                dfs(i, j)
                cnt += 1
    
    print(cnt)