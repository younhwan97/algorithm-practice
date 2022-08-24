import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

target = arr.index(max(arr))
total = 0

while len(arr) > 1:
    if target == 0:
        total += abs(arr[target] - arr[target + 1])
    elif target == len(arr) - 1:
        total += abs(arr[target] - arr[target - 1])
    else:
        min_rank = max(arr[target - 1], arr[target + 1])
        total += abs(arr[target] - min_rank)
    arr.remove(arr[target])
    target = arr.index(max(arr))

print(total)