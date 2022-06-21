A, B = map(int, input().split())
n = int(input())
arr = list()

for _ in range(n):
    arr.append(int(input()))

dif = abs(B - A)

for i in range(0, len(arr)):
    if abs(arr[i] - B) < dif:
        dif = abs(arr[i]- B) + 1
        A = arr[i]

print(dif)