from re import S
import sys
from collections import deque

## 입력
A, B, C = map(int, sys.stdin.readline().split())

## 탐색 메서드 정의
def search(start):
    a = 0
    b = 0
    c = start

    ## 큐 생성
    que = deque()
    que.append((a, b, c))

    ## 반복
    while que:
        aa, bb, cc = que.popleft()

        ## 가능한 액션 정의
        ### 1. aa -> bb
        ### 2. aa -> cc
        ### 3. bb -> cc
        ### 4. bb -> aa
        ### 5. cc -> aa
        ### 6. cc -> bb

        dx = [aa, bb, cc]

        for i in range(6):
            for j in range(6):
                if dx[i] != dx[j]:
                    nx = dx[i] + dx[j]

