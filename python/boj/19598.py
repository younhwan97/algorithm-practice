import sys, heapq
input = sys.stdin.readline

def solve():
    N = int(input())

    arr = list()
    for _ in range(N):
        start, end = map(int, input().split())
        arr.append((start, end))
    arr.sort()

    room = []
    for start, end in arr:
        if len(room) == 0:
            heapq.heappush(room, end)
        else:
            last = heapq.heappop(room)

            if end < last:
                heapq.heappush(room, last)
                heapq.heappush(room, end)
            else:
                if start >= last:
                    heapq.heappush(room, end)
                else:
                    heapq.heappush(room, last)
                    heapq.heappush(room, end)
    
    print(len(room))

solve()