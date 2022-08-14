import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

## 입력 및 그래프 생성
n = int(input())

graph = []

for _ in range(n):
    temp = list(input().strip())
    temp = list(map(int, temp))
    graph.append(temp)

## 탐색 메서드 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def search(x, y):
    global number

    visited[x][y] = True
    graph[x][y] = number 

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if graph[nx][ny] != 0 and not visited[nx][ny]:
                search(nx, ny)

## 탐색
visited = [[False] * n for _ in range(n)]

number = 1
answer = list()
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and not visited[i][j]:
            search(i, j)
            number += 1

print(graph)