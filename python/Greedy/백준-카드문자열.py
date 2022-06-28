T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(input().split())
    answer = list()

    for i in range(N):
        if i == 0:
            answer.append(arr[0])
        else:
            if arr[i] <= answer[0]:
                answer.insert(0, arr[i])
            else:
                answer.append(arr[i])

    print(''.join(answer))