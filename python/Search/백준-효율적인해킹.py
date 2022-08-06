import sys
from collections import deque

input = sys.stdin.readline

## 입력 및 그래프 생성
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

## 탐색 과정에서 사용할 큐
que = deque()

## 탐색 메서드 정의
def search(cnt):
    while que:
        v = que.popleft()

        for i in graph[v]:
            if i not in visited:
                cnt += 1
                visited.add(i)
                que.append(i)
    return cnt

## 탐색
ans = 0
result = []
visited = set()

for i in range(1, N + 1):
    visited.add(i)
    que.append(i)

    cnt = search(0)

    if cnt > ans:
        ans = cnt
        result.clear()
        result.append(i)
    elif cnt == ans:
        result.append(i)

    visited.clear()

for i in range(0, len(result)):
    print(result[i], end=' ')