import sys
sys.setrecursionlimit(10 ** 6)

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N)]
for _ in range(M): 
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

## 탐색 메서드 정의
def search(v, length):
    if length == 4:
        print(1)
        exit()

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            search(i, length + 1)
            visited[i] = False

## 탐색
visited = [False] * N

for i in range(N):
    visited[i] = True
    search(i, 0)
    visited[i] = False

print(0)