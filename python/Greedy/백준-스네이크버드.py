N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

for i in range(0, len(arr)):
    if L >= arr[i]:
        L += 1
    else:
        break

print(L)