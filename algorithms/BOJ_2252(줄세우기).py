from collections import deque
import sys
input = sys.stdin.readline

# 입력 및 그래프 생성
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1) # 진입 차수
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    in_degree[e] += 1

# 위상 정렬
result = []
def topology_sort():
    que = deque()
    
    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            que.append(i)
    
    # 위상정렬의 완전히 수행되기 위해 정확히 N개의 노드를 방문
    for _ in range(N):
        # N개를 방문하기 전에 큐가 비어있게 된다면 -> 사이클 발생
        if not que: return
        
        next = que.popleft()
        result.append(next)

        # 연결되어 있는 노드의 진입차수를 1 빼준다.
        for node in graph[next]:
            in_degree[node] -= 1
            # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
            if in_degree[node] == 0:
                que.append(node)

topology_sort()
print(" ".join(map(str, result)))