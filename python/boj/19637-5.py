import sys
input = sys.stdin.readline

def bs(title, target):
    start, end = 0, len(title) - 1
    ans = 0
    while start <= end:
        mid = (start + end) // 2

        if target > title[mid][0]:
            start = mid + 1
        elif target <= title[mid][0]:
            end = mid - 1
            ans = mid
    return ans

N, M = map(int, input().split())
title = list()
for _ in range(N):
    name, value = input().split() 
    title.append((int(value), name))

for _ in range(M):
    target = int(input())
    print(title[bs(title, target)][1])