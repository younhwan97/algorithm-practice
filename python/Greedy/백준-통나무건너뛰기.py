T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    arr_pre = list()
    arr_post = list()

    for i in range(0, len(arr)):
        if i % 2 == 0:
            arr_pre.append(arr[i])
        else:
            arr_post.append(arr[i])
    
    arr_post.reverse()
    arr_answer = arr_pre + arr_post
    
    answer = abs(arr_answer[0] - arr_answer[len(arr_answer) - 1])
    for i in range(0, len(arr_answer)):
        if i + 1 < len(arr_answer):
            if abs(arr_answer[i] - arr_answer[i + 1]) > answer:
                answer = abs(arr_answer[i] - arr_answer[i + 1])
     
    print(answer)