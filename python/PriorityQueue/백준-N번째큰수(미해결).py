from queue import PriorityQueue
import sys

N = int(input())
pq = PriorityQueue()

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))

    for j in range(N - i - 1, N):
        pq.put(-1 * temp[j])

for i in range(N):
    if i + 1 == N:
        print(-1 * pq.get())
    else:
        pq.get()