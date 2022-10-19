import sys
input = sys.stdin.readline

ans = 0

def search(graph, n, m, x, y, dir):
    global ans
    if graph[x][y] == 0:
        ans += 1
    graph[x][y] = 2

    if dir == 0: # 북
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
    elif dir == 1: # 동
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
    elif dir == 2: # 남
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
    elif dir == 3: # 서 
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 0:
                # 아직 청소가 안됐을 때
                if (dx[i], dy[i]) == (1, 0): new_dir = 2
                elif (dx[i], dy[i]) == (-1, 0): new_dir = 0
                elif (dx[i], dy[i]) == (0, 1): new_dir = 1
                elif (dx[i], dy[i]) == (0, -1): new_dir = 3

                search(graph, n, m, nx, ny, new_dir)
                return

    if dir == 0: x += 1 
    elif dir == 1: y -= 1
    elif dir == 2: x -= 1
    elif dir == 3: y += 1

    if (0 <= x < n) and (0 <= y < m):
        if graph[x][y] == 0 or graph[x][y] == 2:
            search(graph, n, m, x, y, dir)
        else:
            return

def solve():
    n, m = map(int, input().split())
    x, y, dir = map(int, input().split())

    graph = []
    for _ in range(n): graph.append(list(map(int, input().split())))

    # 시작
    search(graph, n, m, x, y, dir)
    
    # 출력
    print(ans)

solve()