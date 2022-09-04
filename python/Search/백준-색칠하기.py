import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def search(num, c):
    global answer 

    color[num] = c
    
    for v in graph[num]:
        if color[v] == 'N':
            if c == 'R':
                search(v, "B")
            else:
                search(v, "R")
        else:
            if color[num] == color[v]:
                answer = "impossible"

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    color = ["N"] * (n + 1)
    answer = "possible"

    for i in range(1, n + 1):
        if color[i] == 'N':
            search(i, 'R')
    
    print(answer)