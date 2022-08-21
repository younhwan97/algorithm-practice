import sys
input = sys.stdin.readline

n = int(input())
arr = list()

for _ in range(n):
    day, deadline = map(int, input().split())
    arr.append((day, deadline))

## 데드라인을 기준으로 내림차순 정렬
arr.sort(key=lambda x: x[1], reverse=True)

## 일을 시작해야하는 날짜
d = arr[0][1]

for i in range(len(arr)):
    day, deadline = arr[i]

    if d > deadline:
        d = deadline - day
    else:
        d -= day

print(d)