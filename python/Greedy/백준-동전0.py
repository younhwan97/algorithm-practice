n, k = map(int, input().split())

arr = list()

for i in range(0, n):
    arr.append(int(input()))


count = 0

## 동전의 가치를 담은 리스트를 내림차순으로 정렬
arr.sort(reverse=True)

for item in arr:
    if k // item != 0:
        count += k // item
        k = k % item

print(count)