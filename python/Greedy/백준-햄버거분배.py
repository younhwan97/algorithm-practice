N, K = map(int, input().split())

arr = list(input())

answer = 0
for i in range(0, N):
    if arr[i] == 'P':
        if i - K >= 0 and i + K + 1 < N:
            for j in range(i - K, i + K + 1):
                if arr[j] == 'H':
                    arr[j] = 'E'
                    answer += 1
                    break
        elif i - K >= 0 and i + K + 1 >= N:
            for j in range(i - K, N):
                if arr[j] == 'H':
                    arr[j] = 'E'
                    answer += 1
                    break
        elif i - K < 0 and i + K + 1 < N:
            for j in range(0, i + K + 1):
                if arr[j] == 'H':
                    arr[j] = 'E'
                    answer += 1
                    break
        elif i - K < 0 and i + K + 1 >= N:
            for j in range(0, N):
                if arr[j] == 'H':
                    arr[j] = 'E'
                    answer += 1
                    break
print(answer)