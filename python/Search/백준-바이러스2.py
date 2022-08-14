import sys

## 입력 및 그래프 생성
input = sys.stdin.readline

n = int(input())
k = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

## 탐색 메서드 정의
def search(v):
    global cnt

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            search(i)

## 탐색
visited = [False] * (n + 1)

cnt = 0
search(1)
print(cnt)