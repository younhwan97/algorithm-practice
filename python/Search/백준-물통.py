import sys
from collections import deque

## 입력
A, B, C = map(int, sys.stdin.readline().split())

## 탐색
## 큐 생성
que = deque()
que.append((0, 0))

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        que.append((x, y))

def search():
    while que:
        a, b = que.popleft()
        c = C - a - b

        if a == 0:
            answer.append(c)

        ## 액션 정의
        ## a -> b
        water = min(a, B - b)
        pour(a - water, b + water)

        ## a -> c
        water = min(a, C - c)
        pour(a - water, b)

        ## b -> a
        water = min(A - a, b)
        pour(a + water, b - water)

        ## b -> c
        water = min(C - c, b)
        pour(a, b - water)

        ## c -> a
        water = min(A - a, c)
        pour(a + water, b)
    
        ## c -> b
        water = min(c, B - b)
        pour(a, b + water)


# 방문 여부(visited[x][y])
visited = [[False] * (B+1) for _ in range(A+1)]
visited[0][0] = True


answer = []

search()

answer.sort()
for i in answer:
    print(i, end=" ")