import sys, itertools
from collections import deque
input = sys.stdin.readline

def find(graph, n, distance, x, y):
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
                if graph[nx][ny] != '-':
                    if distance[nx][ny] == -1:
                        distance[nx][ny] = distance[a][b] + 1
                        que.append((nx, ny))
                    else:
                        if distance[a][b] + 1 < distance[nx][ny]:
                            distance[nx][ny] = distance[a][b] + 1
                            que.append((nx, ny))
                    
def solve():
    n, k = map(int, input().split())
    graph = []
    for _ in range(n): graph.append(list(map(int, input().split())))

    position = []
    new_graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1: # 벽
                new_graph[i][j] = '-'

            if graph[i][j] == 2: # 바이러스
                position.append((i, j))
                new_graph[i][j] = '*'
    
    # 조합
    com = itertools.combinations(position, k)
    ans = 10000
    for c in com:
        distance = [[-1] * n for _ in range(n)]

        # 활성화 될 바이러스 표시
        for position in c:
            x, y = position
            new_graph[x][y] = '#'
        
        # 바이러스 확산
        for i in range(n):
            for j in range(n):
                if new_graph[i][j] == '#':
                    distance[i][j] = 0
                    find(new_graph, n, distance, i, j)

        # 바이러스 활성화 상태 초기화
        for position in c:
            x, y = position
            new_graph[x][y] = '*'   

        for i in range(n):
            for j in range(n):
                if new_graph[i][j] == '*':
                    distance[i][j] = 0
    
        pass_loop = False
        for i in range(n):
            for j in range(n):
                if not (new_graph[i][j] == '*' or new_graph[i][j] == '#' or new_graph[i][j] == '-'):
                    if distance[i][j] == -1:
                        pass_loop = True
                        break
            if pass_loop:
                break

        if not pass_loop:
            max_value = max(map(max, distance))
            ans = min(ans, max_value)
        
    if ans == 10000:
        print(-1)
    else:
        print(ans)

solve()