import sys
sys.setrecursionlimit(10 ** 6)

## 입력
N, R, Q = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

query = []
for _ in range(Q): query.append(int(sys.stdin.readline()))

## 탐색 메서드 정의
def search(v):
    result[v] = 1
    
    for i in graph[v]:
        if result[i] == 0:
            search(i)
            result[v] += result[i]
    
## 탐색
result = [0] * (N + 1)
search(R)

for i in query:
    print(result[i])