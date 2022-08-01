import sys

## 입력
n = int(sys.stdin.readline())

arr = [[] for _ in range(2)]
for i in range(2):
    if i == 0:
        for i in range(1, n + 1):
            arr[0].append(i)
    else:
        for _ in range(n):
            arr[1].append(int(sys.stdin.readline()))

print(arr)