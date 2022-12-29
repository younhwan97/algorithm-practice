import sys, heapq
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = []
    pq = []

    for _ in range(n):
        num, start, end = map(int, input().split())

        arr.append((start, end, num))

    arr.sort()
    classes = [0] * (n + 1)

    room_num = 1
    for start, end, num in arr:
        if not pq:
            heapq.heappush(pq, (end, num))
            classes[num] = room_num
            room_num += 1
        else:
            e, n = heapq.heappop(pq)

            if e <= start:
                heapq.heappush(pq, (end, num))
                classes[num] = classes[n]
        
            else:
                heapq.heappush(pq, (e, n))
                heapq.heappush(pq, (end, num))
                classes[num] = room_num
                room_num += 1
    
    print(len(pq))

    for i in range(1, len(classes)):
        print(classes[i])

solve()