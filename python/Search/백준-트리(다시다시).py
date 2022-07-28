import sys
sys.setrecursionlimit(10 ** 6)

## 입력 및 그래프 생성
n = int(sys.stdin.readline())
temp = list(map(int, sys.stdin.readline().split()))
target_node = int(sys.stdin.readline())

graph = [[] for _ in range(n)]
root_node_num = -1
for i in range(n):
    if temp[i] == -1:
        ## 루트 노드
        root_node_num = i
    else:
        parent_node_num = temp[i]
        child_node_num = i
        
        graph[parent_node_num].append(child_node_num)
        graph[child_node_num].append(parent_node_num)

## 탐색 메서드
def search(v, target):
    visited[v] = True

    for i in graph[v]:
        if not visited[i] and i != target:
            result_graph[v].append(i)
            result_graph[i].append(v)
            search(i, target)

## 결과 그래프의 리프 노드를 탐색하는 메서드
def search2(v):
    global answer

    visited[v] = True

    if len(result_graph[v]) == 1 and v != root_node_num:
        answer += 1
    
    for i in result_graph[v]:
        if not visited[i]:
            search2(i)

    ## 루트 노드만 남은 경우 = 루트노드가 단말 노드가 된 경우
    if answer == 0:
        answer += 1

## 탐색
if target_node == root_node_num:
    print(0)
else:
    visited = [False] * n
    result_graph = [[] for _ in range(n)]
    search(root_node_num, target_node)

    answer = 0
    visited = [False] * n
    search2(root_node_num)
    print(answer)