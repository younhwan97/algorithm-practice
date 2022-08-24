import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

dif = list()
dif.append(arr2[0] - arr[0])

for i in range(1, n):
    print(dif)
    if dif[len(dif) - 1] > 0:
        if arr2[i] - arr[i] > 0:
            if arr2[i] - arr[i] > dif[len(dif) - 1]:
                dif[len(dif) - 1] = arr2[i] - arr[i]
        else:
            dif.append(arr2[i] - arr[i])
    else:
        if arr2[i] - arr[i] < 0:
            if arr2[i] - arr[i] < dif[len(dif) - 1]:
                dif[len(dif) - 1] = arr2[i] - arr[i]
        else:
            dif.append(arr2[i] - arr[i])
print(dif)
cnt = 0
for i in range(len(dif)):
    cnt += abs(dif[i])

print(cnt)


## 4 3 5 7 9
## 4 3 5  7 9
## 4 3 5  7 9 6
## 4 5 6  7 9 8   3