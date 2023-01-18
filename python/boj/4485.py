import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, distance, N):
    distance[0][0] = graph[0][0]

    que = deque()
    que.append((0, 0))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]  
    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < N) and(0 <= ny < N):
                if distance[nx][ny] == -1:
                    distance[nx][ny] = distance[a][b] + graph[nx][ny]
                    que.append((nx, ny))
                else:
                    if distance[nx][ny] > distance[a][b] + graph[nx][ny]:
                        distance[nx][ny] = distance[a][b] + graph[nx][ny]
                        que.append((nx, ny)) 

problem = 1
while True:
    N = int(input())

    if N == 0:
        break

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    distance = [[-1] * N for _ in range(N)]
    bfs(graph, distance, N)

    print("Problem " + str(problem) + ": " + str(distance[N - 1][N - 1]))
    problem +=1
