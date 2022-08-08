N = int(input())
maximum_weight = list(map(int, input().split()))

M = int(input())
box_weight = list(map(int, input().split()))

if max(maximum_weight) < max(box_weight):
    ## 크레인으로 옮길 수 없는 상자가 존재하는 경우
    print(-1)
else:
    ## 가장 처리할 수 있는 무게가 적은 크레인부터 가장 무게가 무거운 박스를 처리할 수 있는지 체크!
    ## 박스는 내림차순
    box_weight.sort(reverse=True)
    ## 크레인은 오름차순
    maximum_weight.sort()

    time = 0
    while box_weight:

        for i in range(0, len(maximum_weight)):
            for j in range(0, len(box_weight)):
                if maximum_weight[i] >= box_weight[j]:
                    del box_weight[j]
                    break
        time += 1
    
    print(time)