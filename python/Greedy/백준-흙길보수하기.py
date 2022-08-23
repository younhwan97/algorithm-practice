import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list()

for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start + 1, end))

arr.sort(key=lambda x:x[1], reverse=True)

cnt = 0
start, end = arr[0]
for i in range(n):
    while end >= start:
        cnt += 1
        end -= l

    if i + 1 < n:
        start = arr[i + 1][0]
        
        if end > arr[i + 1][1]:
            end = arr[i + 1][1]

print(cnt)