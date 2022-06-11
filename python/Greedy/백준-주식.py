T = int(input())
answer_arr = list()

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    answer_1 = 0
    paid_cost = 0
    cnt = 0
    for i in range(0, len(arr)):
        if i + 1 < len(arr):
            if arr[i] <= arr[i + 1]:
                ## 존버
                paid_cost += arr[i]
                cnt += 1
            else:
                ## 익절
                if paid_cost != 0 and cnt != 0:
                    answer_1 += (arr[i] * cnt - paid_cost)
                    cnt = 0
                    paid_cost = 0
        else:
            answer_1 += (arr[i] * cnt - paid_cost)
    
    answer_arr.append(answer_1)

for item in answer_arr:
    print(item)