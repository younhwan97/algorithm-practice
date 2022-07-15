N = int(input())
maximum_weight = list(map(int, input().split()))

M = int(input())
box_weight = list(map(int, input().split()))

if max(maximum_weight) < max(box_weight):
    ## 크레인으로 옮길 수 없는 상자가 존재하는 경우
    print(-1)
else:
    ## 23 32 25 28 => 23, 25, 28, 32
    ## 5 27 10 16 24 20 2 32 18 7 => 2, 5, 7, 10, 16, 18, 20, 24, 27, 32

    maximum_weight.sort()
    box_weight.sort()
    arr = [[] for _ in range(N)]

    index = 0

    while box_weight:
        for i in range(N):
            if box_weight:
                if box_weight[index] <= maximum_weight[i]:
                    arr[i].append(box_weight[index])
                    del box_weight[index]
            else:
                break

        index = 0
    
    needed_minute = len(arr[0])

    for i in range(0, len(arr)):
        if needed_minute < len(arr[i]):
            needed_minute = len(arr[i])

    print(arr)