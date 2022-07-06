import sys, heapq

N, H, T = map(int, sys.stdin.readline().split())

pq = []

for _ in range(N):
    height = int(sys.stdin.readline())
    heapq.heappush(pq, -1 * height)

pass_validation_check = True
using_item_cnt = 0

for cnt in range(1, T + 1):
    temp_height = -1 * heapq.heappop(pq)

    if temp_height < H and temp_height >= 1:
        pass_validation_check = True
        using_item_cnt = cnt - 1
        break

    if temp_height == 1:
        pass_validation_check = False
        heapq.heappush(pq, -1)
        break
    else:
        temp_height = int(temp_height / 2)
        using_item_cnt = cnt

        if temp_height <= 1:
            pass_validation_check = False
            heapq.heappush(pq, -1)
            break
        else:
            if temp_height >= H:
                heapq.heappush(pq, -1 * temp_height)

if pass_validation_check == False:
    print("NO")
    print(-1 * heapq.heappop(pq))
else:
    if len(pq) == 0:
        print("YES")
        print(using_item_cnt)
    else:
        max = -1 * heapq.heappop(pq)

        if max >= H:
            print("NO")
            print(max)
        else:
            print("YES")
            print(using_item_cnt)