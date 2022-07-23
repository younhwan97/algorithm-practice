import sys

def search(graph, visited, v, e):
    global temp

    visited[v] = True

    for i in graph[v]:
        if not visited[i[0]]:
            temp += i[1]

            if i[0] == e:
                break
            
            search(graph, visited, i[0], e)
    
n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, w = map(int, sys.stdin.readline().split())

    graph[a].append((b, w))
    graph[b].append((a, w))

for i in range(len(graph)):
    graph[i].sort(reverse=True)

visited = [False] * (n + 1)

## 바닥 노드를 구한다.
child_node = []

for i in range(1, n + 1):
    if len(graph[i]) == 1:
        child_node.append(i)

max = 0
for i in range(0, len(child_node)):

    for j in range(0, len(child_node)):
        temp = 0
        search(graph, visited, child_node[i], child_node[j])

        visited = [False] * (n + 1)

        if temp > max:
            max = temp
        
        break
    break

print(max)