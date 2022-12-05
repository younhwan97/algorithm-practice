import sys, heapq
input = sys.stdin.readline

def solve():
    cnt = int(input())
    tmp = list()

    for _ in range(cnt):
        start, end = map(int, input().split())
        tmp.append((start ,end))

    tmp.sort()

    end_time = -1
    ans = 1
    for start, end in tmp:
        if end_time == -1:
            end_time = end
        else:
            if start >= end_time:
                end_time = end
                ans += 1
            elif end < end_time:
                end_time = end
                
    print(ans)

solve()