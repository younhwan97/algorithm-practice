import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, w, h):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, 1, -1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < h) and (0 <= ny < w):
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny, w, h)

answer = list()

while True:
    w, h = map(int, input().split())
    graph = [[] for _ in range(h)]
    cnt = 0

    if w == 0 and h == 0:
        break
    else:
        for i in range(0, h):
            temp = list(map(int, input().split()))
            graph[i] = temp
        
        for i in range(h):
            for j in range(w):
                if graph[i][j] > 0:
                    dfs(i, j, w, h)
                    cnt +=1
        
        print(cnt)