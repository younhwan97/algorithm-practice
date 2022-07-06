import sys, heapq

N = int(sys.stdin.readline())
pq = []

for _ in range(N):
    number, level = map(int, sys.stdin.readline().split())
    heapq.heappush(pq, (-1 * level, -1 * number))

M = int(sys.stdin.readline())

for _ in range(M):
    cmd = sys.stdin.readline()

    if "add" in cmd:
        cmd, number, level = cmd.split()
        number = int(number)
        level = int(level)

        heapq.heappush(pq, (-1 * level, -1 * number))
    elif "recommend" in cmd:
        cmd, number = cmd.split()
        number = int(number)

        if number == 1:
            temp = heapq.heappop(pq)
        

    else:
        cmd, number = cmd.split()