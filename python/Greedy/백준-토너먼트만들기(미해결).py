import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dif = list()
for i in range(n):
    if i + 1 < n:
        dif.append(abs(arr[i + 1] - arr[i]))

cost = 0
while dif:
    index = dif.index(min(dif))

    cost += dif[index]
    arr[index] = arr[index + 1] if arr[index + 1] < arr[index] else arr[index]

    del arr[index + 1]

    dif = list()
    for i in range(len(arr)):
        if i + 1 < len(arr):
            dif.append(abs(arr[i + 1] - arr[i]))
            
print(cost)