from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, end, store, visited):
    # 큐 생성
    que = deque()
    que.append(start)

    while que:
        x, y = que.popleft()

        if abs(x - end[0]) + abs(y - end[1]) <= 1000:
            return True

        # 이동
        for i in range(len(store)):
            nx, ny = store[i]

            if abs(nx - x) + abs(ny - y) <= 1000:
                if not visited[i]:
                    que.append((nx, ny))
                    visited[i] = True

    return False

def solve():
    T = int(input())

    for _ in range(T):
        N = int(input())
    
        start_x, start_y = map(int, input().split())
        store = []
        for _ in range(N):
            x, y = map(int, input().split())
            store.append((x, y))
        end_x, end_y = map(int, input().split())

        visited = [False] * (N)
        res = bfs((start_x, start_y), (end_x, end_y), store, visited)

        if res:
            print("happy")
        else:
            print("sad")
solve()