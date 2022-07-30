import sys
from collections import deque

## 입력 및 그래프 생성
N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

## 탐색 메서드 정의
def search(start):
    ## 큐 생성
    que = deque()
    que.append(start)

    ## 너비 우선 탐색
    while que:
        v = que.popleft()

        for i in graph[v]:
            if result[i] == -1:
                que.append(i)
                result[i] = result[v] + 1
            
## 탐색
result = [-1] * (N + 1)
result[X] = 0
search(X)

## 결과
answer = []

for i in range(0, len(result)):
    if result[i] == K:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()

    for i in range(0, len(answer)):
        print(answer[i])