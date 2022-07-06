import sys, heapq

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    pq_min = []
    pq_max = []

    visited = [False] * N
    key = 0

    for _ in range(N):
        oper, value = sys.stdin.readline().split()
        value = int(value)

        if oper == "I":
            heapq.heappush(pq_min, (value, key))
            heapq.heappush(pq_max, (-1 * value, key))
            key += 1
        elif oper == "D":
            if value == 1:
                while pq_max and visited[pq_max[0][1]]:
                    heapq.heappop(pq_max)

                if pq_max:
                    visited[pq_max[0][1]] = True
                    heapq.heappop(pq_max)
            else:
                while pq_min and visited[pq_min[0][1]]:
                    heapq.heappop(pq_min)

                if pq_min:
                    visited[pq_min[0][1]] = True
                    heapq.heappop(pq_min)
    
    while pq_max and visited[pq_max[0][1]]:
        heapq.heappop(pq_max)
    while pq_min and visited[pq_min[0][1]]:
        heapq.heappop(pq_min)
    
    if pq_max and pq_min:
        max = -1 * heapq.heappop(pq_max)[0]
        min = heapq.heappop(pq_min)[0]
        print(max, min)
    else:
        print("EMPTY")