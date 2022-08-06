import sys

## 입력 및 그래프 생성
input = sys.stdin.readline

N, M = map(int, input().split())

graph_1 = []
graph_2 = []

for _ in range(N): graph_1.append(list(map(int, input().split())))
for _ in range(N): graph_2.append(list(map(int, input().split())))

## 탐색 메서드 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def search(x, y, value, origin_value):
    visited[x][y] = True

    graph_1[x][y] = value

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if not visited[nx][ny] and graph_1[nx][ny] == origin_value:
                search(nx, ny, value, origin_value)

## 탐색
visited = [[False] * M for _ in range(N)]

finish_loof = False
for i in range(N):
    for j in range(M):
        if graph_1[i][j] != graph_2[i][j]:
            value = graph_2[i][j]
            search(i, j, value, graph_1[i][j])
            finish_loof = True
            break
    if finish_loof:
        break

## 결과
if graph_1 == graph_2:
    print("YES")
else:
    print("NO")