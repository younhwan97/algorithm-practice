import sys, heapq

N, K = map(int, sys.stdin.readline().split())

jewell = []
bag = []

for _ in range(N):
    weight, price = map(int, sys.stdin.readline().split())
    heapq.heappush(jewell, (-1 * price, weight))

for _ in range(K):
    max_weight = int(sys.stdin.readline())
    heapq.heappush(bag, max_weight)

answer = []

while jewell:
    temp = heapq.heappop(jewell)
    price = -1 * temp[0]
    weight = temp[1]

    

    # temp = []
    # while bag:
    #     bag_weight = heapq.heappop(bag)

    #     if bag_weight >= weight:
    #         answer.append(price)
    #         break
    #     else:
    #         temp.append(bag_weight)

    # for i in range(0, len(temp)):
    #     heapq.heappush(bag, temp[i])

print(sum(answer))