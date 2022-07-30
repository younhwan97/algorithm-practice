import sys
from collections import deque

## 입력
A, B, N, M = map(int, sys.stdin.readline().split())

## 탐색 메서드 정의
def search(start):
    result[start] = 0

    ## 큐 생성
    que = deque()
    que.append(start)

    ## 반복
    while que:
        v = que.popleft()

        ## 8가지 이동 방식 정의
        ## 6, 7 인덱스는 배수로 
        jump_method = [1, -1, A, B, -A, -B, A, B]

        for i in range(8):
            if i == 6 or i == 7:
                nx = v * jump_method[i]
            else:
                nx = v + jump_method[i]
            
            if (0 <= nx <= 100_000):
                if result[nx] == -1:
                    que.append(nx)
                    result[nx] = result[v] + 1

            if nx == M:
                return 

## 결과
result = [-1] * 100_001

## 탐색
search(N)
print(result[M])
