import sys
from collections import deque

## 입력
N, M = map(int, sys.stdin.readline().split())
jump = [-1] * 101

for _ in range(N + M):
    a, b = map(int, sys.stdin.readline().split())
    jump[a] = b

## 탐색 메서드 정의
def search(start):
    result[start] = 0

    ## 큐
    que = deque()
    que.append(start)

    ## 반복
    while que:
        x = que.popleft()

        for i in range(1, 7):   
            nx = x + i

            if nx <= 100:
                if jump[nx] != -1:
                    if result[jump[nx]] == -1:
                        ## 해당 위체에 첫 방문인 경우   
                        result[jump[nx]] = result[x] + 1
                        que.append(jump[nx])
                    else:
                        ## 중복 방문인 경우
                        if result[jump[nx]] > result[x] + 1:
                            result[jump[nx]] = result[x] + 1
                            que.append(jump[nx])
                    
                    if result[nx] == -1:
                        ## 해당 위치에 첫 방문인 경우
                        result[nx] = result[x] + 1
                    else:
                        ## 중복 방문의 경우
                        if result[nx] > result[x] + 1:
                            result[nx] = result[x] + 1
                else:
                    if result[nx] == -1:
                        ## 해당 위치에 첫 방문인 경우
                        result[nx] = result[x] + 1
                        que.append(nx)
                    else:
                        ## 중복 방문의 경우
                        if result[nx] > result[x] + 1:
                            result[nx] = result[x] + 1
                            que.append(nx)

## 탐색
result = [-1] * 101
search(1)
print(result[100])