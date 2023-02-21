import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, price = map(int, input().split())
    graph[start].append((end, price))

start, end = map(int, input().split())

def dijkstra(start):
    global graph, distance

    # 초기화
    distance[start] = 0

    # 시작점을 우선순위 큐에 넣는다
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        price, current = heapq.heappop(pq)

        if distance[current] < price: continue
        for v, price2 in graph[current]:
            if price + price2 < distance[v]:

                distance[v] = price + price2
                heapq.heappush(pq, (distance[v], v))
        
distance = [1000000000] * (N + 1)
dijkstra(start)
print(distance[end])

# -> 기본 bfs 시간 초과
# from collections import deque
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# graph = [[] for _ in range(N + 1)]

# for _ in range(M):
#     start, end, price = map(int, input().split())
#     graph[start].append((end, price))

# start, end = map(int, input().split())
# distance = [-1] * (N + 1)

# def bfs(start):
#     global graph, distance

#     distance[start] = 0

#     que = deque()
#     que.append(start)

#     while que:
#         a = que.popleft()

#         for v, price in graph[a]:
#             if distance[v] == -1:
#                 distance[v] = distance[a] + price
#                 que.append(v)
#             else:
#                 if distance[v] > distance[a] + price:
#                     distance[v] = distance[a]+ price
#                     que.append(v)

# bfs(start)
# print(distance[end])