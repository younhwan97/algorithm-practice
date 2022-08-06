import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque

## 입력 및 그래프 생성
graph = []

for _ in range(5):
    graph.append(list(sys.stdin.readline().split()))

## 탐색 메서드 정의
def search(x, y, cnt, s):
    if cnt == 6:
        if s not in result:
            result.append(s)
        return
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < 5) and (0 <= ny < 5):
            search(nx, ny, cnt + 1, s + graph[nx][ny])

## 탐색
result = list()

for i in range(5):
    for j in range(5):
        search(i, j, 1, graph[i][j])
        

print(len(result))