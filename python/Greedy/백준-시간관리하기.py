import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    time, deadline = map(int, input().split())
    arr.append((time, deadline))

arr.sort(key=lambda x: x[1], reverse=True)

time = arr[0][1]

for i in range(0, len(arr)):
    need, deadline = arr[i]

    if time > deadline:
        time = deadline - need
    else:
        time -= need
    
if time >= 0:
    print(time)
else:
    print(-1)