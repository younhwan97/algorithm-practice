import sys
sys.setrecursionlimit(10**6)

def search(graph, visited, x, y, R, C):
    global answer
    global max

    visited.append(graph[x][y])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < R) and (0 <= ny < C):
            if graph[nx][ny] != -1 and graph[nx][ny] not in visited:
                answer += 1
                temp = graph[nx][ny]
                graph[nx][ny] = -1
                search(graph, visited, nx, ny, R, C)
                graph[nx][ny] = temp

                if answer > max:
                    max = answer
                    answer = 0
                visited.clear()
                visited.append(graph[0][0])

R, C = map(int, sys.stdin.readline().split())

graph = []

for _ in range(R):
    temp = list(sys.stdin.readline())
    graph.append(temp)

answer = 1
visited = []
max = 1

search(graph, visited, 0, 0, R, C)
print(max)