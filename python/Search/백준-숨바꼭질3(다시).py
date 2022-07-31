import sys
from collections import deque

## 입력
N, K = map(int, sys.stdin.readline().split())

## 탐색 메서드 정으
def search(start):
    result[start] = 0

    ## 큐
    que = deque()
    que.append(start)
    
    ## 반복
    while que:
        x = que.popleft()

        ## 순간이동을 하는 경우
        if (0 <= 2 * x <= 100_000):
            if result[2 * x] == -1:
                result[2 * x] = result[x]
                que.append(2 * x)
            else:
                if result[x] < result[2 * x]:
                    result[2 * x] = result[x]
                
        ## 일반 이동을 하는 경우
        dx = [1, -1]

        for i in range(2):
            nx = x + dx[i]

            if (0 <= nx <= 100_000):
                if result[nx] == -1:
                    result[nx] = result[x] + 1
                    que.append(nx)
                else:
                    if result[x] + 1 < result[nx]:
                        result[nx] = result[x] + 1

## 탐색
result = [-1] * 100_001
search(N)
print(result[K])