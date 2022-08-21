import sys
input = sys.stdin.readline

t = int(input())

for k in range(t):
    n, m = map(int, input().split())
    arr = list()

    book = [0] * (n + 1)

    for _ in range(m):
        start, end = map(int, input().split())
        arr.append((start, end))

    arr.sort(key=lambda x: x[1])

    cnt = 0
    for i in range(len(arr)):
        start, end = map(int, arr[i])

        for j in range(start, end + 1):
            if book[j] == 0:
                book[j] = 1
                cnt += 1
                break
    
    print(cnt)