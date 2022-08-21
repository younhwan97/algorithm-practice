import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dif = list()

for i in range(len(arr)):
    if i + 1 < len(arr):
        dif.append(arr[i + 1] - arr[i])

dif.sort(reverse=True)
print(sum(dif[k - 1:]))