import sys
sys.setrecursionlimit(10 ** 6)

cnt = 0

def search(graph, v, visited):
    global cnt
    
    cnt += 1
    for i in range(len(graph)):
        if not visited[i]:
            a, b = graph[i]
            if a == v:
                visited[i] = True
                search(graph, b, visited)
            elif b == v:
                visited[i] = True
                search(graph, a, visited)
    

def solution(n, wires):
    global cnt
    
    answer =  1000000
    for i in range(len(wires)):
        new_wires = wires[:i] + wires[i + 1:]
        visited = [False] * len(new_wires)
        cnt = 0
        search(new_wires, wires[i][0], visited)
        answer = min(answer, abs(cnt - (n - cnt)))

    return answer