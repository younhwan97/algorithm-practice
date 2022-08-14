import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

## 탐색 메서드 정의
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def search(x, y):
    visited[x][y] = True

    ## 8방향 탐색
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < h) and (0 <= ny < w):
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                search(nx, ny)
    
while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break
    else:
        ## 그래프 생성
        graph = []

        for _ in range(h):
            temp = list(map(int, input().split()))
            graph.append(temp)
        
        ## 탐색
        visited = [[False] * w for _ in range(h)]

        cnt = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1 and not visited[i][j]:
                    cnt += 1
                    search(i, j)

        print(cnt)