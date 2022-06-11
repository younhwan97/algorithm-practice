import sys

N = int(input())
arr = list()

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)
answer = 0
for i in range(0, len(arr)):
    if i + 2 < len(arr) and arr[i] < arr[i + 1] + arr[i + 2]:
        answer = arr[i] + arr[i + 1] + arr[i + 2]
        break

if answer == 0:
    print(-1)
else:
    print(answer)