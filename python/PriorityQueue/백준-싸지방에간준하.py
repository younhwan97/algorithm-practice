import sys, heapq

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    arr.append((s, e))

arr.sort()

pq = []
number = 1
for i in range(len(arr)):
    if not pq:
        heapq.heappush(pq, (arr[i][1], number, 1))
        number += 1
    else:
        temp_arr = []

        while pq:
            temp = heapq.heappop(pq)
            e = temp[0]
            cnt = temp[2]
            origin_number = temp[1]

            if arr[i][0] >= e:
                temp_arr.append((origin_number, e, cnt))
            else:
                heapq.heappush(pq, (e, origin_number, cnt))
                break
        temp_arr.sort()
        if temp_arr:
            heapq.heappush(pq, (arr[i][1], temp_arr[0][0], temp_arr[0][2] + 1))
            del temp_arr[0]
        else:
            heapq.heappush(pq, (arr[i][1], number, 1))
            number += 1

        for i in range(len(temp_arr)):
            heapq.heappush(pq, (temp_arr[i][1], temp_arr[i][0], temp_arr[i][2]))
        
answer = [[] for _ in range(len(pq))]

while pq:
    temp = heapq.heappop(pq)
    index = temp[1]
    cnt = temp[2]
    answer[index - 1] = cnt

print(len(answer))
for i in range(len(answer)):
    if i + 1 != len(answer):
        print(answer[i], end=" ")
    else:
        print(answer[i])