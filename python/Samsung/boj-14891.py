import sys
input = sys.stdin.readline


def cycle(target, dir, arr):
    ## 우측
    if target + 1 <= 3:
        if arr[target][2] != arr[target + 1][6]:
            cycle(target + 1, -1 * dir, arr)
    ## 좌측
    if target - 1 >= 0:
        if arr[target][6] != arr[target - 1][2]:
            cycle(target - 1, -1 * dir, arr)

    new_arr = list()
    if dir == 1:
        new_arr.append(arr[target][-1])

        for i in range(7):
            new_arr.append(arr[target][i])    
    else:
        for i in range(1, 8):
            new_arr.append(arr[target][i])    
        
        new_arr.append(arr[target][0])

    arr[target] = new_arr
    
def solve():
    # 입력
    arr = []
    for _ in range(4): arr.append(list(input().strip()))

    k = int(input())
    method = []

    for _ in range(k):
        target, dir = map(int, input().split())
        method.append((target - 1, dir))

    # 맞닿는 부분 2, 6
    for i in range(len(method)):
        target, dir = method[i]
        cycle(target, dir, arr)
        break

    print(arr)

solve()