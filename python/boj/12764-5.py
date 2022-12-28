import sys,heapq
input = sys.stdin.readline

def solve():
    n = int(input())

    arr = []
    pq = []
    count = [0] * (n + 1)

    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr.sort()

    index = 0
    used = [False] * (n + 1)

    for i in range(0, 1_000_000):
        # 종료조건
        if index >= len(arr):
            break
        
        # 싸지방 이용을 마친 원소를 큐에서 제거
        if pq:
            end, n = heapq.heappop(pq)

            if end == i:
                used[n] = False
            else:
                heapq.heappush(pq, (end, n))

        if arr[index][0] == i:
            for num in range(1, n + 1):
                if not used[num]:
                    break
            
            heapq.heappush(pq, (arr[index][1], num))
            used[num] = True
            count[num] += 1
            index += 1
        else:
            pass

    ans = 0
    result = []
    for i in range(1, len(count)):
        if count[i] == 0:
            break
        else:
            ans += 1
            result.append(count[i])

    print(ans)
    for i in range(len(result)):
        print(result[i], end = " ")

solve()