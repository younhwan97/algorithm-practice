import sys, itertools
input = sys.stdin.readline

def paint(graph, n, m, x, y, dir, p):
    if not ((0 <= x < n) and (0 <= y < m)):
        return

    if graph[x][y] == 6:
        return
    
    if graph[x][y] == 0 and p:
        graph[x][y] = '#'
    elif graph[x][y] == '#' and not p:
        graph[x][y] = 0

    if dir == 1: # 동
        paint(graph, n, m, x, y + 1, dir, p)
    elif dir == 2: # 남
        paint(graph, n, m, x + 1, y, dir, p)
    elif dir == 3: # 서
        paint(graph, n, m, x, y - 1, dir, p)
    elif dir == 4: # 북
        paint(graph, n, m, x - 1, y, dir, p)
    elif dir == 5: # 동서
        paint(graph, n, m, x, y + 1, 1, p)
        paint(graph, n, m, x, y - 1, 3, p)
    elif dir == 6: # 남북
        paint(graph, n, m, x - 1, y, 4, p)
        paint(graph, n, m, x + 1, y, 2, p)
    elif dir == 7: # 북동
        paint(graph, n, m, x - 1, y, 4, p)
        paint(graph, n, m, x, y + 1, 1, p)
    elif dir == 8: # 동남
        paint(graph, n, m, x, y + 1, 1, p)
        paint(graph, n, m, x + 1, y, 2, p)
    elif dir == 9: # 서남
        paint(graph, n, m, x, y - 1, 3, p)
        paint(graph, n, m, x + 1, y, 2, p)
    elif dir == 10: # 서북
        paint(graph, n, m, x, y - 1, 3, p)
        paint(graph, n, m, x - 1, y, 4, p)
    elif dir == 11: # 북동서
        paint(graph, n, m, x, y + 1, 1, p)
        paint(graph, n, m, x, y - 1, 3, p)
        paint(graph, n, m, x - 1, y, 4, p)
    elif dir == 12: # 북동남
        paint(graph, n, m, x - 1, y, 4, p)
        paint(graph, n, m, x, y + 1, 1, p)
        paint(graph, n, m, x + 1, y, 2, p)
    elif dir == 13: # 남동서
        paint(graph, n, m, x, y + 1, 1, p)
        paint(graph, n, m, x + 1, y, 2, p)
        paint(graph, n, m, x, y - 1, 3, p)
    elif dir == 14: # 북서남
        paint(graph, n, m, x - 1, y, 4, p)
        paint(graph, n, m, x + 1, y, 2, p)
        paint(graph, n, m, x, y - 1, 3, p)
    elif dir == 15: # 동서남북
        paint(graph, n, m, x, y + 1, 1, p)
        paint(graph, n, m, x - 1, y, 4, p)
        paint(graph, n, m, x + 1, y, 2, p)
        paint(graph, n, m, x, y - 1, 3, p)

ans = 8 * 8 + 1

def find(graph, n, m, visited):
    global ans

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1

    ans = min(ans, cnt)

    for i in range(n):
        for j in range(m):
            if graph[i][j] != '#' and (1 <= graph[i][j] <= 5) and not visited[i][j]:
                visited[i][j] = True

                if graph[i][j] == 1:
                    for k in range(1, 5):
                        paint(graph, n, m, i, j, k, True)
                        find(graph, n, m, visited)
                        paint(graph, n, m, i, j, k, False)
                elif graph[i][j] == 2:
                    for k in range(5, 7):
                        paint(graph, n, m, i, j, k, True)
                        find(graph, n, m, visited)
                        paint(graph, n, m, i, j, k, False)
                elif graph[i][j] == 3:
                    for k in range(7, 11):
                        paint(graph, n, m, i, j, k, True)
                        find(graph, n, m, visited)
                        paint(graph, n, m, i, j, k, False)
                elif graph[i][j] == 4:
                    for k in range(11, 15):
                        paint(graph, n, m, i, j, k, True)
                        find(graph, n, m, visited)
                        paint(graph, n, m, i, j, k, False)
                elif graph[i][j] == 5:
                    paint(graph, n, m, i, j, 15, True)
                    find(graph, n, m, visited)
                    paint(graph, n, m, i, j, 15, False)

                visited[i][j] = False
        
def solve():
    global ans
    n, m = map(int, input().split())
    graph = []
    for _ in range(n): graph.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]

    find(graph, n, m, visited)
    print(ans)

solve()