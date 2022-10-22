import sys
input = sys.stdin.readline

def air(graph, r, c, air_cleaner_start):
    new_graph= [[0] * c for _ in range(r)]

    for i in range(0, air_cleaner_start + 1):
        if i == 0:
            for j in range(0, len(graph[i]) - 1):
                new_graph[0][j] = graph[0][j + 1] 
            new_graph[0][-1] = graph[i + 1][-1]
        elif i == air_cleaner_start:
            for j in range(2, len(graph[i])):
                new_graph[i][j] = graph[i][j - 1]
        else:
            new_graph[i][0] = graph[i - 1][0]
            new_graph[i][-1] = graph[i + 1][-1]
            
            for j in range(1, len(graph[i]) - 1):
                new_graph[i][j] = graph[i][j]
    
    for i in range(air_cleaner_start + 1, r):
        if i == air_cleaner_start + 1:
            for j in range(2, len(graph[i])):
                new_graph[i][j] = graph[i][j - 1]
        elif i + 1 == r:
            for j in range(0, len(graph[i]) - 1):
                new_graph[i][j] = graph[i][j + 1]
            new_graph[i][-1] = graph[i - 1][-1]
        else:
            new_graph[i][0] = graph[i + 1][0]
            new_graph[i][-1] = graph[i - 1][-1]

            for j in range(1, len(graph[i]) - 1):
                new_graph[i][j] = graph[i][j]

    return new_graph

def next(graph, r, c):
    new_graph= [[0] * c for _ in range(r)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0 and graph[i][j] != -1:
                cnt = 0 # 확산된 방향의 개수
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if (0 <= nx < r) and (0 <= ny < c):
                        if graph[nx][ny] != -1:
                            cnt += 1
                            new_graph[nx][ny] += (graph[i][j] // 5)

                new_graph[i][j] += graph[i][j] - graph[i][j] // 5 * cnt 
    return new_graph

def solve():
    r, c, t = map(int, input().split())

    graph = []

    for _ in range(r):
        graph.append(list(map(int, input().split())))

    air_cleaner_start = -1

    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                air_cleaner_start = i
                break
        if air_cleaner_start != -1:
            break

    # 시작
    for _ in range(t):
        graph = next(graph, r, c)
        graph = air(graph, r, c, air_cleaner_start)

    # 결과
    ans = 0
    for i in range(r):
        ans += sum(graph[i])

    print(ans)
solve()