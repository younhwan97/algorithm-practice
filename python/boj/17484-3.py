import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# dp로 다시 풀어볼 것

dx = [1, 1, 1]
dy = [0, -1, 1]
ans = 601

def search(graph, x, y, N, M, cost, used):
    global ans

    if x == N:
        ans = min(ans, cost)
        return

    for i in range(3):
        if used != i:
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx <= N) and (0 <= ny < M):
                search(graph, nx, ny, N, M, cost + graph[x][y], i)


N, M = map(int, input().split())
graph = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

for i in range(M):
    search(graph, 0, i, N, M, 0, -1)

print(ans)