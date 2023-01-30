import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

ans = 10_000

def search(info, positon, move, D):
    global ans

    if positon >= D:
        if positon == D: 
            ans = min(ans, move)
        return
    
    for start, end, distance in info:
        if positon <= start:
            is_moved = True
            search(info, end, min(distance, end - start) + (start - positon) + move, D)
        elif positon > start:
            pass
    
    search(info, D, move + (D - positon), D)

N, D = map(int, input().split())
arr = list()
for _ in range(N):
    start, end, distance = map(int, input().split())
    arr.append((start, end, distance))

search(arr, 0, 0, D)
print(ans)