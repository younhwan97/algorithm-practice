import sys
sys.setrecursionlimit(10 ** 6)

## 탐색 메서드 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def search(x, y, step):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == 0 and graph[nx][ny] > graph[x][y]:
                step += 1
                visited[nx][ny] = step
                search(nx, ny, step)
    
## 입력 및 그래프 생성
n = int(sys.stdin.readline())

graph = []
for _ in range(n): graph.append(list(map(int, sys.stdin.readline().split())))

## 탐색
max_value = 0

for i in range(n):
    for j in range(n):
        visited = [[0] * n for _ in range(n)]

        search(i, j, 0)

        temp_max = max(map(max, visited))

        if temp_max > max_value:
            max_value = temp_max

print(max_value - 1)