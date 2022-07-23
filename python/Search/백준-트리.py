import sys

def search(graph, visited, v, k):
    global answer

    if v == k:
        return

    if len(graph[v]) == 1:
        answer += 1

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            search(graph, visited, i, k)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

graph = [[] for _ in range(n)]

for i in range(0, len(arr)):
    if arr[i] != -1:
        graph[i].append(arr[i])
        graph[arr[i]].append(i)

k = int(sys.stdin.readline())

visited = [False] * (n)

answer = 0

search(graph, visited, 0, k)

print(answer)