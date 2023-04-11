import sys, heapq
input = sys.stdin.readline

# 입력 및 그래프 생성
N = int(input())
INF = 10_000 * 100_000
energy = [0] * (N + 1) # 개미의 남은 에너지
position = [i for i in range(N + 1)] # 개미의 위치
graph = [[] for _ in range(N + 1)] 
for i in range(1, N + 1):
    energy[i] = int(input())
for _ in range(N - 1):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

# dijkstra를 통해 1번 노드에서 각 노드까지의 거리를 구한다.
distance = [INF] * (N + 1)
def dijkstra(start):
    pq = []
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distance[node]: continue
        for e, c in graph[node]:
            if c + dist < distance[e]:
                distance[e] = c + dist
                heapq.heappush(pq, (c + dist, e))
dijkstra(1)

# 에너지가 남은 개미가 없을 때 까지 개미를 움직인다.
def check_finish():
    for i in range(2, N + 1):
        if energy[i] > 0:
            return False
    return True

while not check_finish():
    for i in range(2, N + 1):
        if energy[i] > 0:
            current = position[i] # 개미의 현재 위치
            next, cost = -1, -1
            for n, c in graph[current]:
                # 거리가 더 가까워지고, 남은 에너지로 갈 수 있을 때
                if distance[n] < distance[current] and energy[i] >= c:
                    next, cost = n, c

            if next != -1 and cost != -1:
                position[i] = next
                energy[i] -= cost
            else:
                energy[i] = 0

# 결과
for i in range(1, N + 1):
    print(position[i])