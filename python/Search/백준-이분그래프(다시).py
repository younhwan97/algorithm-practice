import sys
sys.setrecursionlimit(10**6)

def search(graph, color, num, new_color):
    color[num] = new_color

    for i in graph[num]:
        if color[i] == -1:
            if new_color == 'R':
                search(graph, color, i, 'B')
            else:
                search(graph, color, i, 'R')

T = int(sys.stdin.readline())

for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(V + 1)]
    color = [-1] * (V + 1)

    for _ in range(E):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1, V + 1):
        if color[i] == -1:
            search(graph, color, i, 'R')
    
    answer = "YES"
    for i in range(1, V + 1):
        for j in graph[i]:
            if color[j] == color[i]:
                answer = "NO"
                break

        if answer == "NO":
            break
    print(answer)