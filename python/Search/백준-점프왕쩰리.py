import sys
input = sys.stdin.readline

n = int(input())

## 입력
graph = []

for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

## 탐색 메서드
dx = [1, 0]
dy = [0, 1]

def search(x, y):
    visited[x][y] = True
    step = graph[x][y]

    if graph[x][y] == -1:
        print("HaruHaru")
        exit()

    for i in range(2):
        nx = x + dx[i] * step
        ny = y + dy[i] * step

        if (0 <= nx < n) and (0 <= ny < n):
            if not visited[nx][ny]:
                search(nx, ny)            

visited = [[False] * n for _ in range(n)]
search(0, 0)
print("Hing")