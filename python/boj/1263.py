import sys, heapq
input = sys.stdin.readline

def solve():
    n = int(input())

    pq = []
    for _ in range(n):
        need, end = map(int, input().split())

        heapq.heappush(pq, (-1 * end, need))

    ans = -1
    while pq:
        end, need = heapq.heappop(pq)
        end = -1 * end

        if ans == -1:
            ans = end - need
        else:
            if ans < end:
                ans -= need
            else:
                ans = end - need
    
    if ans >= 0:
        print(ans)
    else:
        print(-1)

solve()