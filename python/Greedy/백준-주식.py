import sys

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))

    ## 최고점
    ## 최고점에 도달하기 전까지는 무조건 매수
    max_price = max(arr)

    answer = 0
    paid_price = 0
    cnt = 0
    if arr == sorted(arr, reverse=True):
        print(0)
    else:
        for i in range(0, len(arr)):
            if i + 1 < len(arr):
                if arr[i] < arr[i + 1]:
                    ## 다음 날 가격이 더 오를 것으로 예상된다면
                    ## 무조건 매수
                    paid_price += arr[i]
                    cnt += 1
                elif arr[i] >= arr[i + 1]:
                    ## 다음 날 가격이 떨어질 것으로 예상된다면
                    if arr[i] == max_price:
                        ## 지금이 최고점일 때
                        ## 손절
                        answer += (max_price * cnt - paid_price)
                        cnt = 0
                        paid_price = 0
                        temp_arr = arr[i + 1:]
                        max_price = max(temp_arr)
                    else:
                        paid_price += arr[i]
                        cnt += 1
            else:
                answer += (arr[i] * cnt - paid_price)
        print(answer)