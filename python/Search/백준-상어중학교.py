from re import search
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

## 입력
n, m = map(int, input().split())

graph = []
for _ in range(n): graph.append(list(map(int, input().split())))

## 탐색 메서드
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, color):
    global temp_cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
            if graph[nx][ny] == color or graph[nx][ny] == 0:
                visited[nx][ny] = True
                temp_cnt += 1
                dfs(nx, ny, color)
                
def dfs2(x, y, color):
    visited[x][y] = True
    graph[x][y] = -2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n) and not visited[nx][ny]:
            if graph[nx][ny] == color or graph[nx][ny] == 0:
                dfs2(nx, ny, color)

## 탐색
score = 0
while True:
    max_group_cnt = -1
    x, y = n - 1, n - 1
    visited = [[False] * n for _ in range(n)]

    ## 그룹을 찾는다.
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if not visited[i][j] and graph[i][j] != -1 and graph[i][j] != -2 and graph[i][j] != 0:
                temp_cnt = 1

                visited[i][j] = True
                dfs(i, j, graph[i][j])

                for k in range(n):
                    for l in range(n):
                        if graph[k][l] == 0 and visited[k][l]:
                            visited[k][l] = False

                if temp_cnt != 1 and temp_cnt >= max_group_cnt:
                    max_group_cnt = temp_cnt
                    x, y = i, j

    ## 종료 조건            
    if max_group_cnt == -1 or max_group_cnt == 1:
        print(score)
        break
    else:
        ## 점수 합산
        score += (max_group_cnt * max_group_cnt)

        ## 블록 제거
        visited = [[False] * n for _ in range(n)]
        dfs2(x, y, graph[x][y])

        ## 중력
        for i in range(1, n):
            for j in range(1, n + 1):
                if graph[n - i - 1][n - j] != -1 and graph[n - i - 1][n - j] != -2:
                    for k in range(n - i, n):
                        if graph[k][n - j] == -2:
                            graph[k][n - j] = graph[k - 1][n - j]
                            graph[k - 1][n - j] = -2
                        else:
                            break
    
        print(graph)
        ## 회전
        temp_graph = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                temp_graph[n - 1 - j][i] = graph[i][j]

        graph = temp_graph[:]
        
        ## 중력
        for i in range(1, n):
            for j in range(1, n + 1):
                if graph[n - i - 1][n - j] != -1 and graph[n - i - 1][n - j] != -2:
                    for k in range(n - i, n):
                        if graph[k][n - j] == -2:
                            graph[k][n - j] = graph[k - 1][n - j]
                            graph[k - 1][n - j] = -2
                        else:
                            break
        
        break