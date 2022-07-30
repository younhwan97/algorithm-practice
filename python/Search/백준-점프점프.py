import sys
from collections import deque

## 입력 및 리스트 생성
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

## 탐색 함수 정의
def search(X):
    result[X] = 0

    ## 큐 생성
    que = deque()
    que.append(X)

    ## 너비 우선 탐색
    while que:
        x = que.popleft()

        step = arr[x]

        if step != 0:
            for i in range(1, step + 1):
                nx = i + x

                if (0 <= nx <= n - 1) and (result[nx] == -1):
                    result[nx] = result[x] + 1
                    que.append(nx)
                
                if nx == n - 1:
                    return

## 결과 리스트 
result = [-1] * (n)

## 탐색
search(0)
print(result[n - 1])