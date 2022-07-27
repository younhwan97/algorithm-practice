import sys
sys.setrecursionlimit(10 ** 6)

def search(v, root, target):
    global answer
    visited[v] = True

    if v != root and len(graph[v]) == 1:
        answer += 1

    for i in graph[v]:
        if i != target and not visited[i]:
            search(i, root, target)

## 입력
n = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

## 그래프 생성
graph = [[] for _ in range(n)]
root_node_number = 0

for i in range(0, len(temp)):
    if temp[i] == -1:
        root_node_number = i
    else:
        node_number = i
        parent_node_number = temp[i]

        graph[parent_node_number].append(node_number)
        graph[node_number].append(parent_node_number)

## 결과
answer = 0

## 탐색
visited = [False] * (n)

if target == root_node_number:
    ## 루트노드를 삭제한다면
    print(0)
else:
    search(root_node_number, root_node_number, target)
    print(answer)