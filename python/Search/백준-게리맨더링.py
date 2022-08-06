import sys
from collections import deque

## 입력 및 그래프 생성
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

graph = []
graph.append([])
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    temp = temp[1:]
    graph.append(temp)

## 탐색 메서드 정의
def search(v, s):
    if dif[v] == -1 or dif[v] > sum(p) - s:
        dif[v] = sum(p) - s

    print(v, s)

    for i in graph[v]:
        if not visited[i]:
            if dif[i] == -1 or dif[i] > sum(p) - (s + p[i - 1]):
                visited[i] = True
                search(i, s + p[i - 1])
                visited[i] = False

## 탐색
visited = [False] * (n + 1)

min_value = sum(p)
for i in range(1, n + 1):
    dif = [-1] * (n + 1)

    visited[i] = True
    search(i, p[i - 1])
    visited[i] = False

    print(dif)
    
    for i in range(0, len(dif)):
        if dif[i] != -1 and min_value > dif[i]:
            min_value = dif[i]
    
    break

print(min_value)
