import sys

input = sys.stdin.readline

## 입력
n = int(input())

arr = [[] for _ in range(2)]
for i in range(2):
    if i == 0:
        for i in range(1, n + 1):
            arr[0].append(i)
    else:
        for _ in range(n):
            arr[1].append(int(input()))

## 그래프 생성
graph = [[] for _ in range(n + 1)]

for i in range(0, n):
    a = arr[0][i]
    b = arr[1][i]

    graph[a].append(b)

## 탐색 메서드 정의
def search(start, v):
    visited[v] = True

    for i in graph[v]:
        if start == i:
            result.append(start)
        elif not visited[i]:
            search(start, i)
    
## 탐색
result = []

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    search(i, i)

print(len(result))
result.sort()
for i in range(0, len(result)):
    print(result[i], end = ' ')