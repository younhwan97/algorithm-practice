import sys
from collections import deque

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    temp = list(sys.stdin.readline().strip())
    graph.append(list(map(int, temp)))

## 탐색 메서드 정의
def search(x, y):
    graph[x][y] = 'PASS'
    visited[x][y] = True
    
    ## 큐 생성
    que = deque()
    que.append((x, y))

    ## 탐색
    while que:
        a, b = que.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and (0 <= ny < M) and (not visited[nx][ny]):
                if graph[nx][ny] == 0 or graph[nx][ny] == 'PASS':
                    que.append((nx, ny))
                    graph[nx][ny] = 'PASS'
                    visited[nx][ny] = True

                    if nx == N - 1:
                        return "YES"

## 탐색
visited = [[False] * M for _ in range(N)]
for i in range(M):
    if graph[0][i] == 0 or graph[0][i] == 'PASS':
        result = search(0, i)

        if result == "YES":
            break
    
        visited = [[False] * M for _ in range(N)]

## 결과
answer = 'NO'

for i in range(M):
    if graph[N-1][i] == 'PASS':
        answer = 'YES'
        break
    
print(answer)