import sys
sys.setrecursionlimit(10 ** 6)

def search(x, y, n, step):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == 0 and graph[nx][ny] > graph[x][y]:
                step += 1
                visited[nx][ny] = step
                search(nx, ny, n, step)
    
## 입력 및 그래프 생성
n = int(sys.stdin.readline())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

## 방문 정보를 담는 리스트 생성
visited = [[0] * n for _ in range(n)]

## 결과
max_value = 0

## 탐색
for i in range(n):
    for j in range(n):
        search(i, j, n, 0)

        temp_max = max(map(max, visited))

        if temp_max > max_value:
            max_value = temp_max

        visited = [[0] * n for _ in range(n)]

print(max_value - 1)