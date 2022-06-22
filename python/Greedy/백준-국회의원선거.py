import sys

N = int(input())
arr = list()

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

cnt = arr[0]
arr = arr[1:]
arr.sort(reverse=True)

if len(arr) != 0:
    max_cnt = max(arr)
else:
    max_cnt = 0


answer = 0
while True:
    if cnt > max_cnt:
        break
    else:
        arr[0] -= 1
        cnt += 1
        arr.sort(reverse=True)
        max_cnt = max(arr)
        answer += 1
        
print(answer)