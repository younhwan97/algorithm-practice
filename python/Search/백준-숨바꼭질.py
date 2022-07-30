import sys
from collections import deque

## 입력
N, M = map(int, sys.stdin.readline().split())

def search(start, end):
    dx = [1, -1, 2]

    que = deque()
    que.append(start)
    result[start] = 0

    if start == end:
        return result[start]
    else:
        while que:
            x = que.popleft()

            for i in range(3):
                if i == 2:
                    nx = x * dx[i]
                else:
                    nx = x + dx[i]

                if (0 <= nx <= 100_000) and (result[nx] == -1):
                    que.append(nx)
                    result[nx] = result[x] + 1
                
                if nx == M:
                    return result[nx]

result = [-1] * 100_001
print(search(N, M))