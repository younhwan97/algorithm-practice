import sys, heapq

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    temp = list(map(int, sys.stdin.readline().split()))

    pq = []

    for i in range(N):
        heapq.heappush(pq, temp[i])

    answer = 1

    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)

        answer *= (a * b)
        heapq.heappush(pq, (a * b))

    print(answer % 1000000007)