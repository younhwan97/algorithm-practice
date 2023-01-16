import sys
from collections import deque
input = sys.stdin.readline

def check(graph, distance, n, size):
    min_distance = 20 * 20 + 1
    x, y = -1, -1

    for i in range(n):
        for j in range(n):
            # distance[i][j] > 0 이 없으면 자기 자신을 잡아먹는 경우 존재
            if distance[i][j] > 0 and (0 < graph[i][j] < size):
                if min_distance > distance[i][j]:
                    min_distance = distance[i][j]
                    x = i
                    y = j

    return min_distance, x, y

def bfs(graph, distance, x, y, n, size):
    distance[x][y] = 0

    que = deque()
    que.append((x, y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < n) and (0 <= ny < n):
                if graph[nx][ny] <= size:
                    if distance[nx][ny] == -1:
                        distance[nx][ny] = distance[a][b] + 1
                        que.append((nx, ny))
                    else:
                        if distance[nx][ny] > distance[a][b] + 1:
                            distance[nx][ny] = distance[a][b] + 1
                            que.append((nx, ny))
        
def solve():
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    size = 2
    cnt = 0
    time = 0

    x, y = -1, -1

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                x, y = i, j
                break
        if x != -1 and y != -1:
            break
    
    while True:
        distance = [[-1] * n for _ in range(n)]
        bfs(graph, distance, x, y, n, size)
        min_distance, nx, ny = check(graph, distance, n, size)

        if min_distance != 401:
            graph[x][y] = 0
            graph[nx][ny] = 9
            cnt += 1
            time += min_distance
            x = nx
            y = ny

            if cnt == size:
                size += 1
                cnt = 0
        else:
            print(time)
            break

solve()