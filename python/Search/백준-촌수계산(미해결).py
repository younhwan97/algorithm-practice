import sys
sys.setrecursionlimit(10**6)

def search(graph, visited, start, end):
    global answer
    answer += 1

    if start == end:
        print(answer)

    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            search(graph, visited, i, end)

N = int(sys.stdin.readline())
a, b = map(int, input().split())
M = int(sys.stdin.readline())

graph = [[] * N for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

answer = -1

search(graph, visited, a, b)