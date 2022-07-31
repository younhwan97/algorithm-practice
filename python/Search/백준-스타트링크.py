import sys
from collections import deque

## 입력
F, S, G, U, D = map(int, sys.stdin.readline().split())

## 탐색 메서드 정의
def search(start):
    result[start] = 0

    ## 큐
    que = deque()
    que.append(start)

    ## 반복
    while que:
        x = que.popleft()

        dx = [U, -D]

        for i in range(2):
            nx = x + dx[i]

            if (1 <= nx <= F):
                if result[nx] == -1:
                    result[nx] = result[x] + 1
                    que.append(nx)
            
            if nx == G:
                return

## 탐색
result = [-1] * (F + 1) 
search(S)

if result[G] == -1:
    print("use the stairs")
else:
    print(result[G])