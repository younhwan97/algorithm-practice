import sys, heapq

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    pq_min = []
    pq_max = []
  
    for _ in range(N):
        oper, value = sys.stdin.readline().split()
        value = int(value)

        if oper == "I":
            heapq.heappush(pq_min, value)
            heapq.heappush(pq_max, -1 * value)
        elif oper == "D":
            if len(pq_min) != 0 and len(pq_max) != 0:
                if value == 1:
                    ## 최댓값 삭제
                    heapq.heappop(pq_max)
                elif value == -1:
                    ## 최솟값 삭제
                    heapq.heappop(pq_min)

                if len(pq_min) == 0 or len(pq_max) == 0:
                    pq_min = []
                    pq_max = []
        
        print("최소 힙은: ")
        print(pq_min)

        print("최대 힙은:")
        print(pq_max)

    if len(pq_min) != 0 and len(pq_max) != 0:
        max = -1 * heapq.heappop(pq_max)
        min = heapq.heappop(pq_min)
        print(max, min)
    else:
        print("EMPTY")