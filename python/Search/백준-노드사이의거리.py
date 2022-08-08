import sys
sys.setrecursionlimit(10 ** 6)

## 입력 및 그래프 생성
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, w = map(int, input().split())
    
    graph[a].append((b, w))
    graph[b].append((a, w))

## 원하는 노드 사이드 거리
req = []

for _ in range(M):
    a, b = map(int, input().split())
    req.append((a, b))

## 탐색 메서드 정의
def search(v, e, length):
    visited[v] = True

    if v == e:
        print(length)
        return

    for i in graph[v]:
        target, weight = i
        if not visited[target]:
            search(target, e, length + weight)

## 탐색
for i in range(0, len(req)):
    v, e = req[i]

    visited = [False] * (N + 1)

    search(v, e, 0)