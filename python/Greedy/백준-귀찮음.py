n = int(input())
arr = list(map(int, input().split()))

length = sum(arr)
arr.sort()

answer = 0

for i in range(0, len(arr)):
    length -= arr[i]
    answer += (arr[i] * length)

print(answer)