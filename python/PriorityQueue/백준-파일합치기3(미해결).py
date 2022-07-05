import sys, heapq
from queue import PriorityQueue

T = int(input())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    heap = []

    for i in range(N):
        heapq.heappush(heap, arr[i])
    
    answer = 0 

    while len(heap) > 1:
        temp = heapq.heappop(heap) + heapq.heappop(heap)
        answer += temp
        heapq.heappush(heap, temp)

    print(answer)

## PriorityQueue 는 시간초과

# T = int(input())
# answer = list()

# for _ in range(T):
#     N = int(sys.stdin.readline())

#     temp = list(map(int, sys.stdin.readline().split()))
#     pq = PriorityQueue()

#     for i in range(N):
#         pq.put(temp[i])

#     if pq.qsize() > 1:
#         temp_answer = 0

#         while pq.qsize() > 1:
#             temp = pq.get() + pq.get()
#             temp_answer += temp
#             pq.put(temp)
            
#         answer.append(temp_answer)
#     elif pq.qsize() == 1:
#         answer.append(pq.get())

# for item in answer:
#     print(item)